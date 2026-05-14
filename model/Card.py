class Card:

    def __init__(self,question,answer,topic):
        self.question = question
        self.answer = answer
        self.topic = topic

    def __str__(self):
        return f"Question : {self.question}, answer : {self.answer}, topic : {self.topic}\n"
