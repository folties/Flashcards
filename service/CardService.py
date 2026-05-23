from model.Card import Card
from config.AppConfig import CARDS_FILE
from util.validators import validate_card_data


class CardService:

    def __init__(self, card_repository, card_storage_service):
        self.card_repository = card_repository
        self.card_storage_service = card_storage_service

    def load_default_cards(self):
        cards = self.card_storage_service.load_cards(CARDS_FILE)
        self.card_repository.set_cards(cards)

    def save_all_cards(self):
        cards = self.card_repository.get_all_cards()
        self.card_storage_service.save_cards(CARDS_FILE, cards)

    def add_card(self, question, answer, topic, category):
        validate_card_data(question, answer, topic, category)

        card = Card(question, answer, topic, category)

        self.card_repository.add_card(card)
        self.save_all_cards()

    def import_cards_from_file(self, filename):
        cards = self.card_storage_service.load_cards(filename)

        if len(cards) == 0:
            return False

        for card in cards:
            self.card_repository.add_card(card)

        self.save_all_cards()
        return True

    def get_all_cards(self):
        cards = self.card_repository.get_all_cards()
        cards.sort(key=lambda card: card.topic.lower())
        return cards

    def find_cards(self, topic, category):
        if category.lower() == "all":
            return self.find_cards_by_topic(topic)

        return self.find_cards_by_topic_and_category(topic, category)

    def find_cards_by_topic(self, topic):
        return [
            card
            for card in self.card_repository.get_all_cards()
            if card.topic.lower() == topic.lower()
        ]

    def find_cards_by_topic_and_category(self, topic, category):
        return [
            card
            for card in self.card_repository.get_all_cards()
            if card.topic.lower() == topic.lower()
            and card.category.lower() == category.lower()
        ]

    def update_card(self, index, question, answer, topic, category):
        validate_card_data(question, answer, topic, category)

        cards = self.card_repository.get_all_cards()

        if index < 0 or index >= len(cards):
            return False

        self.card_repository.update_card(index, question, answer, topic, category)
        self.save_all_cards()

        return True

    def delete_card(self, index):
        cards = self.card_repository.get_all_cards()

        if index < 0 or index >= len(cards):
            return False

        self.card_repository.delete_card(index)
        self.save_all_cards()

        return True