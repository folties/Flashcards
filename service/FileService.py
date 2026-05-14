from model.Card import Card


class FileService:

    def read_cards_from_file(self, filename):
        cards = []

        with open(filename, "r") as file:
            for line in file:
                question, answer, topic = line.strip().split(",")

                cards.append(Card(question,answer,topic))

        return cards

    def append_card_to_file(self, filename, card):
        with open(filename, "a") as file:
            file.write(f"{card.question},{card.answer},{card.topic}\n")