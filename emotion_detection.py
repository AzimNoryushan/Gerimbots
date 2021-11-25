import malaya
import re

class Emotion_detection:

    def __init__(self):
        self.message = ""

    def getEmotion(self, message):
        model = malaya.emotion.multinomial()
        emotion = model.predict(message)
        message = ' '.join(message)

        with open("DISCORD_CONVERSATION.txt", "a+") as file_object:
            file_object.write(message + "\t" + str(emotion) + "\n")

        return emotion