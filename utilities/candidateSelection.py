import random
from datetime import datetime, timedelta
import pandas as pd
import utilities

class CandidateSelection:

    def __init__(self):
        self.rows = []
        self.df = pd.DataFrame()
        self.skills_list = ["'python'", " 'pyspark'"," 'aws'", " 'docker'", " 'sql'"," 'mysql'"," 'apache-spark-sql'"]
        self.date = datetime
        self.reputation = 500
        self.hireable = True
        self.pythonReposCount = random.randint(13,21)
        self.tweet = ""
        self.repoCount = random.randint(49,99)
        self.user_skill = []
        self.user_hirelable = []
        self.user_reputation = []
        self.user_repo = []
        self.user_date = []
        self.user_tweet = []
        self.skillCount = 0

    def csv_load_to_df(self):
        # mongo = Mongo_Connection()
        mongo_Dataframe = utilities.Mongo_Upload()
        # mongo.collection.insert_many(mongo.csv_to_json('../data_files/final.csv', header=0))
        self.df = mongo_Dataframe.upload()

    def remove_duplicates(self, list1):
        final_list = list(dict.fromkeys(list1))
        return final_list

    def selection(self):
        self.df['tags'] = self.df['tags'].str.strip('[]').str.split(',')
        for i in range(0, len(self.df.tags)):
            self.skillCount = 0
            for j in range(0, len(self.skills_list)):
                if(self.skills_list[j] in self.df.tags[i]):
                    self.skillCount += 1
                if self.skillCount >= 3:
                    self.user_skill.append(self.df.owner_display_name[i])
        self.user_skill = self.remove_duplicates(self.user_skill)
        print(len(self.user_skill))

    def selection_Hireable(self):
        for i in range(0, len(self.df.hireable)):
            for j in range(0, len(self.user_skill)):
                if(self.user_skill[j] in self.df.owner_display_name[i] and bool(self.df.hireable[i]) == self.hireable):
                    self.user_hirelable.append(self.df.owner_display_name[i])
        self.user_hirelable = self.remove_duplicates(self.user_hirelable)
        print(self.user_hirelable)

    def selection_Reputation(self):
        for i in range(0, len(self.df.owner_reputation)):
            for j in range(0, len(self.user_hirelable)):
                if(self.df.owner_reputation[i] != ''):
                    if(self.user_hirelable[j] in self.df.owner_display_name[i] and int(float(self.df.owner_reputation[i])) > self.reputation):
                        self.user_reputation.append(self.df.owner_display_name[i])
        self.user_reputation = self.remove_duplicates(self.user_reputation)
        print(len(self.user_reputation))
    
    def selection_repo(self):
        for i in range(0, len(self.df.public_repos)):
            for j in range(1, len(self.user_reputation)):
                if(self.user_reputation[j] in self.df.owner_display_name[i] and int(float(self.df.public_repos[i])) > self.repoCount and int(float(self.df.python_Repositories[i])) > self.pythonReposCount):
                    self.user_repo.append(self.df.owner_display_name[i])
        self.user_repo = self.remove_duplicates(self.user_repo)
        print(len(self.user_repo))

    def selection_date(self):
        for i in range(0, len(self.df.last_activity_date)):
            for j in range(1, len(self.user_repo)):
                startDate = datetime(2021,9,1).date()
                endDate = datetime.now()
                endDate = endDate.strftime("%d-%m-%Y")
                endDate = datetime.strptime(endDate, '%d-%m-%Y').date()
                if (self.user_repo[j] in self.df.owner_display_name[i] and startDate < datetime.strptime(self.df.last_activity_date[i],'%d-%m-%Y').date() < endDate and startDate < datetime.strptime(self.df.updated_at[i],'%d-%m-%Y').date() < endDate and startDate < datetime.strptime(self.df.tweetData[i],'%d-%m-%Y').date() < endDate):
                    self.user_date.append(self.df.owner_display_name[i])
        self.user_date = self.remove_duplicates(self.user_date)
        print(len(self.user_date))
    

    def selection_tweet(self):
        for i in range(0, len(self.df.tweet)):
            for j in range(1, len(self.user_date)):
                if (self.user_date[j] in self.df.owner_display_name[i] and ("Python" in str(self.df.tweet[i]) or "python" in str(self.df.tweet[i]))):
                    self.user_tweet.append(self.df.owner_display_name[i])
        self.user_tweet = self.remove_duplicates(self.user_tweet)
        print(len(self.user_tweet))
        return self.user_tweet