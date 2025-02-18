import os
from github import Github
# set the variables (token and organization name)
GITHUB_TOKEN = os.getenv("SECRET_TOKEN_REPOS")
GITHUB_ORG = "emilytqin"
REPO_FILE = "docs/repos.md"

# function using pygithub api to access all the repos in GITHUB_ORG
def fetch_repos():
    g = Github(GITHUB_TOKEN)
    org = g.get_organization(GITHUB_ORG)
    repos = org.get_repos()
    # returns a list of the hyperlinks of the repos in this organization
    return (repo.html_url for repo in repos)

# function to update repos.md with all the repos
def update_repos(list_of_repos):
    repo_page = open(REPO_FILE, "a")
    repo_page.write ("# Repositories \n\n")
    for link in list_of_repos:
        repo_page.write(f"- {link}\n")
    repo_page.close()

if __name__ == "__main__":
    repos = fetch_repos()
    update_repos(repos)