import os
from howdoi import howdoi

class Hdi:
    def __init__(self):
        self.question = ""

    def execute(self, question):
        # stream = os.popen('howdoi ' + question)
        # output = stream.read()
        result = howdoi.howdoi(question)
        
        return result
