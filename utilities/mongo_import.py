import pandas as pd
from pymongo import MongoClient
import json

class Mongo_Connection:

    def __init__(self):
        self.client = MongoClient('mongodb+srv://lolwa:lolwa123@cluster0.eoopj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self.database = self.client.BDP1
        self.collection = self.database.final_test

    def csv_to_json(self, filename, header=None):
        data = pd.read_csv(filename, header=header)
        return data.to_dict('records')

#print(csv_to_json('../data/final.csv'))
# if __name__ == '__main__':
#     mongo = Mongo_Connection()
#     mongo.collection.insert_many(mongo.csv_to_json('../data_files/final.csv', header=0))