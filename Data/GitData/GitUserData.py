import csv
import time
import requests
import json
import base64
from github import Github
from pprint import pprint

import pandas as pd
#invalid-\
def gitUserData():
    # read specific columns of csv file using Pandas
    df = pd.read_csv("C:/Users/AKHILESH/Desktop/Bigdata/One data/Sets/numpy-3.csv", usecols=['author.login'])
    print(df)

    g = Github("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")
    count = 0
    header=True
    for i in range(len(df)):
        count+=1
        username = (df['author.login'][i])

        try:

            url = f"https://api.github.com/users/{username}"
                # make the request and return the json

            users_d=g.get_user(username)

            user_data = requests.get(url).json()
            pythoncount=0

            for repo in users_d.get_repos():

                if repo.language == 'Python':
                    pythoncount += 1
            diction = {'python Repositories': pythoncount}

            user_data = {**user_data , **diction}
            print(user_data)
            c = pd.DataFrame([user_data], columns=user_data.keys())


            c.to_csv('../gituser_data.csv', mode='a',index=False, header=header)
            header=False
        except:
            pass
        time.sleep(60)

gitUserData()
