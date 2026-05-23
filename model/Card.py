class Card:

    def __init__(self, question, answer, topic, category):
        self.question = question
        self.answer = answer
        self.topic = topic
        self.category = category

    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "topic": self.topic,
            "category": self.category
        }

    @staticmethod
    def from_dict(data):
        return Card(
            data["question"],
            data["answer"],
            data["topic"],
            data["category"]
        )

    def __str__(self):
        return (
            f"Question: {self.question}, "
            f"Answer: {self.answer}, "
            f"Topic: {self.topic}, "
            f"Category: {self.category}"
        )