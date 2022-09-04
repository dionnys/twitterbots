#!/opt/homebrew/opt/python@3.10/bin/python3
# # -*- coding: utf-8 -*-
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


def image(api):
    #https://developer.twitter.com/en/docs/twitter-api/v1/media/upload-media/uploading-media/media-best-practices
    file_image = './photos/input.jpeg'
    media = api.media_upload(file_image)
    print('media_ids:', media.media_id_string)
    api.update_status(media_ids=[media.media_id_string], status=date)

def main():
    api = create_api()
    while True:
        image(api)
        logger.info("Waiting...")
        time.sleep(120)

if __name__ == "__main__":
    main()