import matplotlib.pyplot as plt
import traceback
from sentiment_detection import Sentiment_detection
from twint_service import Twint_service
from datetime import date
import time

class Topic_sentiment():

    def __init__(self):
        self.topic = ""

    def listToString(self, list):
        string = str(list).replace(' ', '')
        string = string.replace('[', '')
        string = string.replace(']', '')
        string = string.replace('\'', '')

        return string

    def analyze_tweet(self, topic):

        positive_results = 0
        negative_results = 0
        neutral_results = 0
        undetected_results = 0

        tweets = Twint_service().getTweets(topic)

        time.sleep(20)

        for tweet in tweets:
            try:
                sentiment = self.listToString(Sentiment_detection().getSentiment([tweet['tweet']]))
                if(sentiment=='positive'):
                    positive_results = positive_results+1
                elif(sentiment=='negative'):
                    negative_results = negative_results+1
                elif(sentiment=='neutral'):
                    neutral_results = neutral_results+1
                else:
                    undetected_results = undetected_results+1
            except:
                print(traceback.print_exc())

        self.generate_chart(positive_results, negative_results, neutral_results, topic)

        return "Positive: " + str(positive_results) + " Negative: " + str(negative_results) + " Neutral: " + str(negative_results)

    def generate_chart(self, positive_results, negative_results, neutral_results, topic):
        try:
            today = date.today()
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            ax.axis('equal')
            sentiment_list = ['positive', 'negative', 'neutral']
            data_count = [positive_results, negative_results, neutral_results]
            colors = ['green', "red", "blue"]
            ax.pie(data_count, labels = sentiment_list,autopct='%1.2f%%',colors=colors)
            plt.title("Sentiment of " + topic + " in Twitter on " +  today.strftime("%d/%m/%Y"))
            plt.savefig('img/plot3.png', dpi=300, bbox_inches='tight')
        except:
            print(traceback.print_exc())
