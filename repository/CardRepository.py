class CardRepository:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def set_cards(self, cards):
        self.cards = cards

    def get_all_cards(self):
        return self.cards

    def update_card(self, index, question, answer, topic, category):
        self.cards[index].question = question
        self.cards[index].answer = answer
        self.cards[index].topic = topic
        self.cards[index].category = category

    def delete_card(self, index):
        self.cards.pop(index)