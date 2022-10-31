#!/opt/homebrew/bin/python3.11
# -*- coding: utf-8 -*-
"""
#Copyright 2022 Dionnys Bonalde.
#https://developer.twitter.com/en/apps/
#https://docs.tweepy.org/en/latest/api.html
"""

from tweepy import API, Cursor, OAuthHandler
import os, configparser
import logging
import time, datetime
date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
from dotenv import load_dotenv
load_dotenv()

def create_api():



    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_key = os.getenv('ACCESS_KEY')
    access_secret = os.getenv('ACCESS_SECRET')

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()

    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
