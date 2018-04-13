# eecs398-python-twitter
Starter code used for live demo of integrating the Twitter API and Python for EECS 398 Winter 2018 at University of Michigan, Ann Arbor

## Requirements

### [tweepy](http://www.tweepy.org)

```
$ pip3 install tweepy
```
- created specifically to pull data from Twitter

- no need to index into large dictionaries or format request URLs

### [matplotlib](https://matplotlib.org/2.2.2/index.html)

```
pip3 install matplotlib
```
- good for plotting data

- "not the best out there, but easy to use" - Amrit


## What's included?

#### ``bot.py`` contains starter code for the Python program

#### ``secret.py`` will hold your API keys and tokens

- you want to keep your API keys secret, which is why they are placed in a separate file from your program.

- if you choose to put your project on GitHub, DO NOT commit ``secret.py``

## How to Generate Twitter API Keys and Tokens

### Go to [https://apps.twitter.com](https://apps.twitter.com)

#### NOTE: You will need a Twitter account from this point on.

- sign into Twitter, then click "Create New App" in the upper right

- fill out the name, description, and website for your applicaiton.  Check the "Developer Agreement" box and finish creating your app!

- under the name of your application, find and click the "Keys and Access Tokens" tab

### Consumer Keys

- located under Applicaiton Settings

- copy and paste these keys into ``secret.py``

### Access Tokens

- scroll down and click "Authorize my Application"

- located under "Your Access Token"

- copy and paste these keys into ``secret.py``


### TODO: import libraries

- ``import tweepy``

- ``import matplotlib``

- ``from secret import *``

### TODO: create a new Twitter session

- check out the tweepy documentation on [getting started](http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html)

- use keys/tokens from ``secret.py`` to create the session

### TODO: user input

- ask the user (you) what hashtag to search

### TODO: search for hashtag

- create new Tweet objects for each result

- we only need the time each tweet was posted, but other data may be useful for debugging or other data analysis

### TODO: graph timestamps from tweets in a histogram

- check out the matplotlib documentation on [histograms](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist) and [subplots](https://matplotlib.org/examples/pylab_examples/subplots_demo.html)

- this is just one analysis you could do on Twitter data

- try something on your own!
