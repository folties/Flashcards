from model.Card import Card
from config.AppConfig import CARDS_FILE


class CardService:

    def __init__(self, card_repository, file_service):
        self.card_repository = card_repository
        self.file_service = file_service

    def add_card(self, question, answer, topic):
        card = Card(question, answer, topic)

        self.card_repository.add_card(card)
        self.file_service.save_card(CARDS_FILE, card)

    def load_cards_from_file(self):
        cards = self.file_service.read_cards_from_file(CARDS_FILE)

        for card in cards:
            self.card_repository.add_card(card)

    def get_all_cards(self):
        return self.card_repository.get_all_cards()