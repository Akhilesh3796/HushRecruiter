# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from stackapi import StackAPI
from datetime import date
import pandas as pd

def stackdata(tagList,from_date,to_date):
  SITE = StackAPI('stackoverflow')
  quesList = []
  for tags in tagList:
    ques = SITE.fetch('questions', fromdate=date.fromisoformat(from_date), todate=date.fromisoformat(to_date),
        min=50, tagged=tags, sort='votes')
    quesList.append(ques)
    df = pd.json_normalize(quesList,record_path =['items'])
    df['last_activity_date'] = pd.to_datetime(df['last_activity_date'], unit='s')
    df = df[df['owner.reputation'].notna()]
    df_items = ['tags', 'last_activity_date', 'owner.reputation', 'owner.display_name', 'title']
    df['tags'] = [','.join(map(str, l)) for l in df['tags']]
    df = df[df_items]

    df.to_csv('../lol.csv')
  return df

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  tagList = [["python", "machine learning", "pandas", "numpy", "pytorch", "scikit", "pyspark", "data visualisation",
              "deep learning"]]
  from_date = '2018-02-04'
  to_date = '2020-03-08'
  stackdata(tagList, from_date, to_date)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
