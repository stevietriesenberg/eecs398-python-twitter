# eecs398-python-twitter

# libraries
from datetime import datetime
from datetime import timedelta
from email.utils import parsedate_tz



# TODO: import additional libraries for this project



# class to hold tweets for debugging       
class Tweet():
    def __init__(self, message_in, user_in, time_in):
        self.message = message_in
        self.user = user_in
        self.time = matplotlib.dates.date2num(time_in)
    def __str__(self):
        return "{} tweeted at {}: {}".format(self.user, self.time, self.message)

# TODO: generate Twitter session



# TODO: ask user for hashtag to search




# TODO: search for hashtag and store results




# store Tweet objects in a list
tweets = []
times = []


# store results




# TODO: graph data from Twitter using matplotlib


