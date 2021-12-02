import malaya

class Sentiment_detection:

    def __init__(self):
        self.message = ""

    def getSentiment(self, message):
        model = malaya.sentiment.multinomial()
        sentiment = model.predict(message)
        message = ' '.join(message)

        # with open("DISCORD_CONVERSATION.txt", "a+") as file_object:
        #     file_object.write(message + "\t" + str(emotion) + "\n")

        return sentiment