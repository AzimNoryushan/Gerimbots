import twint
import traceback

class Twint_service:

    def __init__(self):
        self.topic = ""

    
    def getTweets(self, topic):
        try:
            config = twint.Config()
            config.Hide_output = True
            config.Search = topic
            config.Limit = 100
            config.Pandas = True

            twint.run.Search(config)

            tweet_df = twint.storage.panda.Tweets_df
            tweet_to_dict = tweet_df.to_dict('records')

            return tweet_to_dict
        except:
            traceback.print_exc