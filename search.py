# # -*- coding: utf-8 -*-

import tweepy
import logging
from twitterconnection import create_api, time, datetime


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
userID = "media_luna7"

def search(api):
    logger.info("search")
    tweets = tweepy.user_timeline(screen_name=userID,
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
    for info in tweets[:3]:
        print("ID: {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")

def main():
    api = create_api()
    while True:
        search(api)
        #logger.info("Waiting...")
        #time.sleep(60)

if __name__ == "__main__":
    main()