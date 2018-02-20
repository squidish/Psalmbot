
import tweepy 
import json
import re
import markovify
from time import sleep

# Consumer keys and access tokens, used for OAuth
# Put your own keys here
consumer_key = '...'
consumer_secret = '...'
access_token = '...'
access_token_secret = '...'
 
#Get the corpus 
# Get raw text as string.
with open("Pslams.txt") as f:
    text = f.read()
    
mystring = text.replace('\n', ' ').replace('\r', '')    
#print(text)
#Build the model.
text_model = markovify.Text(text)
#Open up twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
  tweet = text_model.make_short_sentence(140)
  #api.update_status(tweet)
  print(tweet)
  sleep(3600)


