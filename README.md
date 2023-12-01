# GGHRstatistics: Get GitHub Repository statistics
Getting statistics from all the GitHub repositories of Kaggle
GitHub Repo Stats

## Functions of main-GGHRS.py
### 1. Main function: Get_GitHub_Repository_statistics(username, token)
This function acts as your personal GitHub investigator, exploring the repositories and collecting their stats. Here's a closer look at how it works:

**Inputs:**  
- username => here is "Kaggle"   
- token => my Git-Hub token (It is needed to have a valid GitHub token with the necessary permissions.)   

**Output:**

statistics of Kaggle repositories:  
- Number of commits, stars, contributors, branches, tags, forks, releases, closed issues, and environments per repository.   
- Number of source code lines per programming language used per repository.

**Key Components:**
- **requests.get(url, headers=headers):** This function sends an HTTP GET request to the specified URL. In our script, it's used to fetch information from GitHub's API.
-**.raise_for_status():** After making a request, this method checks if the request was successful. If there's an issue (like a 404 or 500 error), it raises an HTTPError, which is caught in the try-except block.
- **.json():** This method converts the response content (usually in JSON format) into a Python dictionary, making it easy to work with in our script.
- **try-except Block:** This is a way to handle errors. If an error occurs during the execution of the code inside the try block, it jumps to the except block, preventing the script from crashing.
   - **Error Types:**   
                  - **requests.exceptions.HTTPError:**   Raised if the HTTP request returns an unsuccessful status code (e.g., 404 Not Found, 500 Internal Server Error). The script prints an error message and continues.  
                  - **requests.exceptions.ConnectionError:** Raised if there's a problem connecting to the server. The script prints an error message and continues.   
                  - **requests.exceptions.Timeout:** Raised if the request times out. The script prints an error message and continues.    
                  - **requests.exceptions.RequestException:** A general exception that catches any other unexpected errors. The script prints an error message and continues.


**Fetching:**
- Fetching stars:
  The number of stars a repository has is obtained by accessing the 'stargazers_count' property in the repository information obtained from the /repos/{username}/{repo_name} endpoint.
- Fetching commits, contributors, branches, tags, forks, releases, closed issues, and deployements:
  The script retrieves deployments for a repository using the /repos/{username}/{repo_name}/deployments endpoint. It then extracts unique environments from deployments to count the number of deployments, providing insights into how the repository is deployed in different environments.
- Fetching environments:
  The number of environments a repository has is determined by counting the unique environments from deployments. Based on my search, there is no way to fetch the number of environments directly without deployments.    
  **note: There are no environments available for Kaggle's GitHub repositories.**   
- Fetching programming languages code lines:    
  - The /repos/{username}/{repo_name}/languages endpoint is employed to gather language statistics for a specific repository.   
  - The response from this endpoint contains data on the lines of code written in each programming language present in the repository.    
  - The script iterates through the languages obtained and accumulates the lines of code per language, providing a comprehensive overview of the project's multilingual composition.

---------------------------------------------------------------------------------------------------------------------------------------
### 2. show_stats(stats, repos) 


 **Inputs:**   
- stats => The output of Get_GitHub_Repository_statistics   
- repos => For using their names in plots  
- skip => For checking if a repository skipped due to conflic or not


 **Output:**   
printing the statistics of Kaggle repositories:  
- Total and median number of commits, stars, contributors, branches, tags, forks, releases, closed issues, and environments.   
- Total and median number of source code lines per programming language used.    
 

**Example Output/ printing statistics:**  
 
![Exampleoutput](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/4503fd12-1f5e-4010-8d1c-852067d85300)    

**Example Output/ showing plots:**
- Showing the number of stats(commits, stars, contributors, branches, tags, forks, releases, closed issues, and environments) per repository in line chart   

![commits](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/b25fc31d-c078-498e-b5c0-6b3e9d87383c)
![branches](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/888451da-9b41-4b76-be6d-0b46e4190ba5)
![tags](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/ebf077b9-f920-4752-82a7-d253e0329c8c)
![stars](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/1f3839a2-5f05-4d40-82bf-a36f8609bc61)
![releases](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/b98666d2-661e-45f4-8408-9ca370249642)
![forks](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/ce9da7c9-4e0e-4c7f-864f-068a65d468a0)
![deployments](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/1cd96380-6a05-4a90-819a-e93c254717c9)
![closed_issues](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/602c0af0-850e-428c-b9ac-1e2830aea86c)
![contributers](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/211b5f57-024f-4a74-810f-6c25449c1dff)

--------------------------------------

 **note: run main-GGHRS.py to get the outputs.**  


## Dependencies (Python libraries)
- statistics
- requests
- matplotlib



