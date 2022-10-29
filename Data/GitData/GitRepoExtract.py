import requests
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import os
from datetime import datetime
github_api = "https://api.github.com"
gh_session = requests.Session()
gh_session.auth = ("Akhilesh3796", "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")
print("working")

def commits_of_repo_github(repo, owner, api):
    commits = []
    next = True
    i = 1
    while next == True:
        url = api + '/repos/{}/{}/commits?page={}&per_page=100'.format(owner, repo, i)
        commit_pg = gh_session.get(url = url)
        commit_pg_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in commit_pg.json()]
        commit_pg_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in commit_pg_list]
        commits = commits + commit_pg_list
        if 'Link' in commit_pg.headers:
            if 'rel="next"' not in commit_pg.headers['Link']:
                next = False
        i = i + 1
    return commits
def create_commits_df(repo, owner, api):
    commits_list = commits_of_repo_github(repo, owner, api)
    return json_normalize(commits_list)

commits = create_commits_df('numpy', 'numpy', github_api)

commits.head()
commits.to_csv("../git_data.csv")
