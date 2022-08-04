#!/usr/bin/python
# # -*- coding: utf-8 -*-
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


def create_api():
    configs = configparser.ConfigParser()
    configs.read('config.conf')
    keys = configs['TWITTER']

    consumer_key = keys['CONSUMER_KEY']
    consumer_secret = keys['CONSUMER_SECRET']
    access_key = keys['ACCESS_KEY']
    access_secret = keys['ACCESS_SECRET']

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
