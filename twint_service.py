import twint
import re
import traceback
import pandas
import json

class Twint_service:

    def __init__(self):
        self.topic = ""

    
    def getTweets(self, topic):
        try:
            config = twint.Config()
            config.Hide_output = True
            config.Search = topic
            config.Limit = 10
            config.Pandas = True

            twint.run.Search(config)

            tweet_df = twint.storage.panda.Tweets_df
            tweet_to_dict = tweet_df.to_dict('records')

            return tweet_to_dict
        except Exception as e:
            traceback.print_exc