from model.Card import Card


class FileService:

    def read_cards_from_file(self, filename):
        cards = []

        try:
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()

                    if line == "":
                        continue
                    parts = line.split(";")

                    if len(parts) != 4:
                        print(f"Invalid line skipped: {line}")
                        continue

                    question, answer, topic, category = parts
                    cards.append(
                        Card(question, answer, topic, category)
                    )

            return cards

        except FileNotFoundError:
            return None

    def read_default_cards_file(self, filename):
        cards = self.read_cards_from_file(filename)

        if cards is None:
            open(filename, "w").close()
            return []

        return cards

    def append_card_to_file(self, filename, card):
        with open(filename, "a") as file:
            file.write(
                f"{card.question},{card.answer},{card.topic},{card.category}\n"
            )

    def rewrite_cards_file(self, filename, cards):
        with open(filename, "w") as file:
            for card in cards:
                file.write(
                    f"{card.question},{card.answer},{card.topic},{card.category}\n"
                )