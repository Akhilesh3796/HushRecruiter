import tweepy as tweepy
from tweepy import *
import csv

class twitterDataFetch:

    def __init__(self):
        self.consumer_key = "gQpLX6jHpQkvnEQm4ZgwHNqS0"
        self.consumer_secret = "dewaj63IDCJyUNhuPeNlnp5i7gNJcjWNfunrkbt83mIZc8mZal"
        self.access_key= "99275917-nAOrKz0hgEHOgWWttiPpyXgVqulmKHMIhQBmntB6z"
        self.access_secret = "wHRpRWqpJuQW8tqvbruy3ZzWXXKp5EazbKF8s6pjReAbw"

    def extractTwitterData(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        
        api = tweepy.API(auth,wait_on_rate_limit=True)
        
        csvFile = open('tweetData.csv', 'a')
        csvWriter = csv.writer(csvFile)
        
        search_words = "#python"      # enter your words
        new_search = search_words + " -filter:retweets"
        
        for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=1000,
                                lang="en",
                                since_id=0).items():
            csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
        print("Done")
    
if __name__ == '__main__':
    tweetData = twitterDataFetch()
    tweetData.extractTwitterData()