from pymongo import MongoClient
# from mongo_import import Mongo_Connection
import utilities

class Question_Update:
    def __init__(self):
        self.client = utilities.Mongo_Connection()
        self.conn = self.client.client

    def update(self, user, question, answer):
        try:
            self.conn
            #conn = MongoClient('mongodb+srv://lolwa:lolwa123@cluster0.eoopj.mongodb.net/BDP1?retryWrites=true&w=majority')
            print("Connected successfully!!!")
        except:
            print("Could not connect to MongoDB")

        # database
        db = self.conn.BDP1

        # Created or Switched to collection names: my_gfg_collection
        self.collection = db.test
        # Insert Data
        emp_rec1 = {
            "user": user,
            "questions": question,
            "answer": answer
        }
        rec_id1 = self.collection.insert_one(emp_rec1)