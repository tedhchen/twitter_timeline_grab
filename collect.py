import json
import logging 
import os
import sys
import re
import numpy as np
import pandas as pd
from tweet_collector import TweetCollector


# Parameters
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## File to write collected data to / if you want to use a db connection to write
## to you have to change the code at the end of this script with your custom
## connection
OUT_FILE = ''
## List of twitter IDs
TWITTER_USERS = [] 
TWITTER_CREDENTIALS = {"access_token": '', 
                       "consumer_key": '',
                       "access_token_secret": '',
                       "consumer_secret": ''}

# Set up logging
logger = logging.getLogger('tweet_collector')
hdlr = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='',
                    filemode='a')

# Data Collection
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
logger.info("Starting data collection")

df = pd.DataFrame({'user_id': TWITTER_USERS})
n_users = df.shape[0]
logger.info(f"Processing {n_users} users")

# Initialize collector 
collector = TweetCollector(TWITTER_CREDENTIALS)

# Collect tweets and dump to OUTFILE
n_tweets_collected = 0
with open(OUT_FILE, 'a+', encoding='utf-8') as outfile:
    for index, row in df.iterrows():
        user = row['user_id']
        # Grab tweets
        try:
            tweets = collector.grab_timeline(user)
        except Exception as e:
            logger.error(f"An exception occurred for handle {user}:\n {e}")
            continue
			
        for t in tweets:
            n_tweets_collected += 1
            json.dump(t._json, outfile)
            outfile.write('\n')

logger.info(f"Collected {n_tweets_collected:,} new tweets")
