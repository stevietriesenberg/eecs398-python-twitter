# eecs398-python-twitter

# libraries
from datetime import datetime
from datetime import timedelta
from email.utils import parsedate_tz

# TODO: import additional libraries for this project
from mysecret import *
import tweepy
import matplotlib
import matplotlib.pyplot as plt

# class to hold tweets for debugging       
class Tweet():
    def __init__(self, message_in, user_in, time_in):
        self.message = message_in
        self.user = user_in
        self.time = matplotlib.dates.date2num(time_in)
    def __str__(self):
        return "{} tweeted at {}: {}".format(self.user, self.time, self.message)

# TODO: generate Twitter session
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


# TODO: ask user for hashtag to search
hashtag = input("Enter a hashtag: #")

# TODO: search for hashtag and store results
search_results = tweepy.Cursor(api.search, q = ("#" + hashtag)).items(500)

# store Tweet objects in a list
tweets = []
times = []

for tweet in search_results:
    new_tweet = Tweet(tweet.text, tweet.user.screen_name, tweet.created_at)
    tweets.append(new_tweet)
    times.append(new_tweet.time)




# TODO: graph data from Twitter using matplotlib
f, axarr = plt.subplots(2, sharex=True)
axarr[0].hist(times)
axarr[0].set_title('#' + hashtag)
axarr[1].hist(times, cumulative = True)
plt.show()






