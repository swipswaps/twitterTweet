import sys
import os
import string
import tweepy


#Keys from Twitter Dev
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

maxCount = 280
tweet = "" 
while (len(tweet)) > maxCount or (len(tweet)) == 0:
   tweet = input("What is your tweet?\n")
api.update_status(tweet)
print("Tweet is being tweeted")


