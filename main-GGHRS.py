from statistics import median
import requests
import matplotlib.pyplot as plt

def Get_GitHub_Repository_statistics(username, token):
    headers = {
        'Authorization': f'Token {token}'
    }

    # Fetching repositories
    repo_url = f'https://api.github.com/users/{username}/repos'
    repositories_response = requests.get(repo_url, headers=headers)

    try:
        repositories_response.raise_for_status()
        repositories = repositories_response.json()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print("Something went wrong!", err)
        return None

    # print('reps:', repositories)

    stats = {
        'commits': [],
        'stars': [],
        'contributors': [],
        'branches': [],
        'tags': [],
        'forks': [],
        'releases': [],
        'closed_issues': [],
        'deployments': [],
        'languages': {}
    }

    with_url = ['commits', 'contributors', 'branches', 'releases', 'tags', 'forks', 'closed_issues', 'deployments']

    if repositories is None:
        return stats

    for repo in repositories:
        repo_name = repo.get('name')
        # print('**repoName:', repo_name)
        if repo_name:

            for fetch_stat in with_url:

                if fetch_stat == 'closed_issues':
                    url = f'https://api.github.com/repos/{username}/{repo_name}/issues?q=is%3Aissue+is%3Aclosed'
                else:
                    url = f'https://api.github.com/repos/{username}/{repo_name}/' + fetch_stat
                response = requests.get(url, headers=headers)

                try:
                    response.raise_for_status()
                    if fetch_stat == 'deployments':
                        # Extracting environments from deployments
                        deployments = response.json()
                        environments = set(deployments['environment'] for deployment in deployments)
                        stats['deployments'].append(len(environments))
                    else:
                        stats[fetch_stat].append(len(response.json()))  # Counting the number of fetch stats
                except requests.exceptions.HTTPError as errh:
                    if response.status_code == 409:
                        print(f"Skipped repository {repo_name} due to conflict.")
                    else:
                        print("HTTP Error:", errh)
                except requests.exceptions.ConnectionError as errc:
                    print("Error Connecting:", errc)
                except requests.exceptions.Timeout as errt:
                    print("Timeout Error:", errt)
                except requests.exceptions.RequestException as err:
                    print("Something went wrong!", err)

            repo_info_url = f'https://api.github.com/repos/{username}/{repo_name}'
            repo_info_response = requests.get(repo_info_url, headers=headers)

            try:
                repo_info_response.raise_for_status()
                repo_info = repo_info_response.json()
                stats['stars'].append(repo_info.get('stargazers_count', 0))



            except requests.exceptions.HTTPError as errh:
                print("HTTP Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
            except requests.exceptions.RequestException as err:
                print("Something went wrong!!!", err)

            # Fetching language statistics for each repository
            languages_url = f'https://api.github.com/repos/{username}/{repo_name}/languages'
            languages_response = requests.get(languages_url, headers=headers)

            try:
                languages_response.raise_for_status()
                languages_data = languages_response.json()
                for lang, lines in languages_data.items():
                    stats['languages'].setdefault(lang, []).append(lines)
            except requests.exceptions.HTTPError as errh:
                print("HTTP Error:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Error Connecting:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout Error:", errt)
            except requests.exceptions.RequestException as err:
                print("Something went wrong!!!!", err)
    return stats


def show_stats(stats):
    print('\n')
    print("\033[94mStatistics for Kaggle repositories:\033[0m")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Commits: {sum(stats['commits'])}")
    print(f"Median Commits: {median(stats['commits'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Stars: {sum(stats['stars'])}")
    print(f"Median Stars: {median(stats['stars'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Contributors: {sum(stats['contributors'])}")
    print(f"Median Contributors: {median(stats['contributors'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Branches: {sum(stats['branches'])}")
    print(f"Median Branches: {median(stats['branches'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Tags: {sum(stats['tags'])}")
    print(f"Median Tags: {median(stats['tags'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Forks: {sum(stats['forks'])}")
    print(f"Median Forks: {median(stats['forks'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Releases: {sum(stats['releases'])}")
    print(f"Median Releases: {median(stats['releases'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Closed Issues: {sum(stats['closed_issues'])}")
    print(f"Median Closed Issues: {median(stats['closed_issues'])}")
    print('\033[95m------------------------------\033[0m')
    print(f"Total Environments: {sum(stats['deployments'])}")
    print(f"Median Environments: {median(stats['deployments'])}")
    print('\033[93m*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_**_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\033[0m')

    # Language Stats
    print("\033[94mSource Code Lines for each Programming Language:\033[0m")

    for lang, lines_list in stats['languages'].items():
        total_lines = sum(lines_list)
        median_lines = median(lines_list)
        print('\033[95m------------------------------\033[0m')
        print(f"{lang}: Total Lines - {total_lines}, Median Lines - {median_lines}")

    print('\033[93m*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_**_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\033[0m')

    # # Showing stats in line chart
    # keys = list(stats.keys())
    # values = list(stats.values())
    #
    # plt.plot(keys, sum(values), marker='o', linestyle='-')
    #
    # plt.xlabel('Stats')
    # plt.ylabel('Values')
    # plt.title('Statistics for Kaggle repositories')
    # plt.show()


if __name__ == "__main__":
    GH_username = "Kaggle"
    GH_token = "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"

    GH_stats = Get_GitHub_Repository_statistics(GH_username, GH_token)

    if GH_stats is not None:
        show_stats(GH_stats)
    else:
        print("Error!!! stats in NONE!")
