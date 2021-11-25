import os

class HowDoI:
    def __init__(self):
        self.question = ""

    def execute(self, question):
        stream = os.popen('howdoi ' + question)
        output = stream.read()
        
        return output
