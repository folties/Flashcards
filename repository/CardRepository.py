class CardRepository:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_all_cards(self):
        return self.cards