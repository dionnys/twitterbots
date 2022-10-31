# # -*- coding: utf-8 -*-
"""
#Copyright 2022 Dionnys Bonalde.
#https://developer.twitter.com/en/apps/
#https://docs.tweepy.org/en/latest/api.html
"""
from tweepy import API, Cursor, OAuthHandler
import logging
from twitterconnection import create_api, time, datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def timeline(api):
    logger.info("Retrieving timeline\n")
    for tweet in Cursor(api.home_timeline).items(100):
        print(f"{tweet.user.name} said:\n {tweet.text}\n")

def main():
    api = create_api()
    while True:
        timeline(api)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()