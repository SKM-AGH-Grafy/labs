__author__ = 'kuban'

import tweepy

consumer_key = '''sFJ42on9pMNIiaG09Cejk8gN1'''
consumer_secret = '''w4tRbPkgVzNR9BAIuSX42ROWFkAhNFS6BYF6mnu6hoGNHFndJ3'''

access_token = '''99775039-18PqbGvfYPMq8FYdngEuDc6uioig2ZJkotni2pOac'''
access_token_secret = '''XNf5SyLFH1JX7oWCYlCafBHsW1OhVLvBJ6SfHZ75YvwrT'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
#
# ids = api.followers_ids("qbahn")
# print(ids)
# for id in ids:
#     user =api.get_user(id)
#     secids = api.followers_ids(id)
#     print(secids)


