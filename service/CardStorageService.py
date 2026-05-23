import json
import os
from model.Card import Card


class CardStorageService:

    def load_cards(self, filename):
        if not os.path.exists(filename):
            self.save_cards(filename, [])
            return []

        with open(filename, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []

        return [Card.from_dict(card_data) for card_data in data]

    def save_cards(self, filename, cards):
        folder = os.path.dirname(filename)

        if folder != "":
            os.makedirs(folder, exist_ok=True)

        data = [card.to_dict() for card in cards]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)