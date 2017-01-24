import nltk
import string
from nltk.corpus import stopwords

class FormatTweets:

    def __init__(self, tweets):
        self.tweets = tweets

    def tokenizeTweets(self):
        tokenized_tweets = []
        for tweet in self.tweets:
            tokenized_tweets.append(nltk.word_tokenize(tweet))
        self.tweets = tokenized_tweets

    def removePunctuation(self):
        self.tweets = [self.filterTweetBy(string.punctuation, tweet) for tweet in self.tweets]

    def removeStopwords(self):
        self.tweets = [self.filterTweetBy(stopwords.words('english'), tweet) for tweet in self.tweets]

    def filterTweetBy(self, this_specified_list_of_words, tweet):
        tweet = [word for word in tweet if word not in this_specified_list_of_words]
        return (tweet)

    def formatByAll(self):
        self.tokenizeTweets()
        self.removePunctuation()
        self.removeStopwords()
