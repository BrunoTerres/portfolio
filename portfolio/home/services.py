import os 
import requests

def get_github():
    url = "https://api.github.com/users/octocat/orgs"
    r = requests.get(url)
    github = r.json()
    github_list = []

    for i in range(len(github['github'])):
        github_list.append(github['github'][i])
    
    return github_list 