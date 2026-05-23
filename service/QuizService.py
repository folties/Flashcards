import random


class QuizService:

    def __init__(self, card_service):
        self.card_service = card_service

    def generate_quiz_cards(self, cards):
        for card in cards:
            yield card

    def print_card(self, text):
        width = 50
        border = "+" + "-" * width + "+"

        print(border)

        lines = self.split_text(text, width)

        for line in lines:
            spaces = width - len(line)
            left_spaces = spaces // 2
            right_spaces = spaces - left_spaces

            print("|" + " " * left_spaces + line + " " * right_spaces + "|")

        print(border)

    def split_text(self, text, width):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= width:
                if current_line == "":
                    current_line = word
                else:
                    current_line += " " + word
            else:
                lines.append(current_line)
                current_line = word

        if current_line != "":
            lines.append(current_line)

        return lines

    def start_quiz(self):
        topic = input("Enter topic: ")
        category = input("Enter category or 'all': ")

        cards = self.card_service.find_cards(topic, category)

        if len(cards) == 0:
            print("No cards found")
            return

        random.shuffle(cards)

        score = 0
        total = len(cards)

        for index, card in enumerate(self.generate_quiz_cards(cards)):
            print()
            print(f"Card {index + 1}/{total}")
            self.print_card(card.question)

            input("Press Enter to show answer...")

            self.print_card(card.answer)

            while True:
                print()
                print("Did you know it?")
                print("1.Correct")
                print("2.Wrong")
                print("3.Exit quiz")

                choice = input("Choose option: ")

                if choice == "1":
                    score += 1
                    break

                elif choice == "2":
                    break

                elif choice == "3":
                    print(f"Quiz stopped. Your result: {score}/{index + 1}")
                    return

                else:
                    print("Invalid choice")

        print()
        print("Quiz finished")
        print(f"Your result: {score}/{total}")