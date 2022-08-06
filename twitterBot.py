#!/usr/bin/python
# # -*- coding: utf-8 -*-
"""
#Copyright 2022 Dionnys Bonalde.
#https://developer.twitter.com/en/apps/
#https://docs.tweepy.org/en/latest/api.html
"""

import re
from os import access
import  requests, os, json, datetime
from unicodedata import name
from PIL import Image
from tweepy import API, Cursor, OAuthHandler

from dotenv import load_dotenv

load_dotenv()

import logging
logger = logging.getLogger()

date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_key = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
twitter_api = API(auth, wait_on_rate_limit=True)

try:
    twitter_api.verify_credentials()

except Exception as e:
    logger.error("Error creating API", exc_info=True)
    raise e
logger.info("API created")



def timeline():

    for tweet in Cursor(twitter_api.home_timeline).items(10):
        print(f"{tweet.user.name} said: {tweet.text}")

def searchtwitter():
    for tweet in twitter_api.search(q="Python", lang="en", rpp=10):
        print(f"{tweet.user.name}:{tweet.text}")

def message():

    twitter_api.update_status(date)

def tweet_Image():
    #https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices


    file_image = './photos/input.jpeg'
    media = twitter_api.media_upload(file_image)
    print('media_ids:', media.media_id_string)
    twitter_api.update_status(media_ids=[media.media_id_string], status=date)

def get_followers():

    followers = twitter_api.get_followers()

    for i in followers:
        print(i)

    #return(followers)
if __name__ == '__main__':
    timeline()
