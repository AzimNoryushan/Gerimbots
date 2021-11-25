import malaya

class Emotion_detection:

    def __init__(self):
        self.message = ""

    def getEmotion(self, message):
        model = malaya.emotion.multinomial()
        emotion = model.predict(message)

        return emotion