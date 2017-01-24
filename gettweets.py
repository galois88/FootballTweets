import tweepy
from tweepy import OAuthHandler
import nltk
from nltk.corpus import stopwords
import string

class Tweets():
    def __init__(self):
        self.consumer_key = 'egKslNdlCC4xQ1TZKe1o7hQ7T'
        self.consumer_secret = 'zGVmGuf9Ohlx42tEb5VdC7cgc3OE7yIaDSgjS5ZOGvt1kgPb2h'
        self.access_token = '759636558676828160-HRHQuOdUlsAZCmsqpLdViIVN1G6tE4j'
        self.access_secret = 'PZjVXuyD5vdLlcwITKuMFRLBHo2jFZBuuiW1LelordMfD'

        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.api = tweepy.API(self.auth)

    def showTweets(self, amount):
        self.tweets = self.getTweets(amount)
        for tweet in tweets:
            print('%s \n' %tweet)

    def getTweets(self, amount):
        self.tweets = []
        for status in tweepy.Cursor(self.api.home_timeline).items(amount):
            self.tweets.append(status.text)
        return (self.tweets)
