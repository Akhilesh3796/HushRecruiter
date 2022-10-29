import pymongo
import pandas as pd
from utilities.mongo_import import Mongo_Connection

class Mongo_Upload:

    def __init__(self):
        self.client = Mongo_Connection()
        self.conn = self.client.client

    def upload(self):
        try:
            self.conn
            #client = pymongo.MongoClient('mongodb+srv://lolwa:lolwa123@cluster0.eoopj.mongodb.net/BDP1?retryWrites=true&w=majority')
        except:
            print('couldnt connect')

        db = self.conn.BDP1
        input_data = db.final_test
        data = pd.DataFrame(list(input_data.find()))
        return data