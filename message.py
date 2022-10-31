#!/opt/homebrew/bin/python3.11
#  -*- coding: utf-8 -*-
"""
#Copyright 2022 Dionnys Bonalde.
#https://developer.twitter.com/en/apps/
#https://docs.tweepy.org/en/latest/api.html
"""
from tweepy import API, Cursor, OAuthHandler
import logging
from twitterconnection import create_api, date, time


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def message(api):
    logger.info("Retrieving timeline\n")
    api.update_status(date)



def main():
    api = create_api()
    while True:
        message(api)
        logger.info("Waiting...")
        time.sleep(120)

if __name__ == "__main__":
    main()