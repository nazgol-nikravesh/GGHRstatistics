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
- skip => For checking if a repository skipped due to an Error or not


 **Output:**   
printing the statistics of Kaggle repositories:  
- Total and median number of commits, stars, contributors, branches, tags, forks, releases, closed issues, and environments.   
- Total and median number of source code lines per programming language used.    
 

**Example Output/ printing statistics:**  
 
![Exampleoutput](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/4503fd12-1f5e-4010-8d1c-852067d85300)    

**Example Output/ showing plots:**
- Showing the number of stats(commits, stars, contributors, branches, tags, forks, releases, closed issues, and environments (from deployments)) per repository in line chart   

![commits](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/d15c4f76-cfa2-4333-9dd3-12625e3e081b)
![stars](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/9882a7e8-3f5a-4cb9-877a-f634ed558b61)
![contributers](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/a73f37ee-5d9f-4237-909d-d638c203ddc8)
![branches](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/f728b0fc-b4a7-4bca-aded-782b36c21187)
![tags](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/5852d117-c7da-48d6-9e50-e418413166b6)
![forks](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/4c8bbf6e-2eb3-4c26-81ed-16deb466d871)
![releases](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/fa53e8da-9655-4e79-a745-9336082f9ac9)
![closed_issues](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/48cbe06a-6a2e-4153-be3a-fbad91db7033)
![deployments](https://github.com/nazgol-nikravesh/GGHRstatistics/assets/93579818/99865406-741e-4667-97cd-ac6c0630c362)

--------------------------------------

 **note: run main-GGHRS.py to get the outputs.**  


## Dependencies (Python libraries)
- statistics
- requests
- matplotlib



