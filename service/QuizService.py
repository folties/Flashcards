import random


class QuizService:

    def __init__(self, card_service):
        self.card_service = card_service

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
        topic = input("Enter topic for quiz: ")

        cards = self.card_service.find_cards_by_topic(topic)

        if len(cards) == 0:
            print("No cards found for this topic")
            return

        random.shuffle(cards)

        score = 0
        total = len(cards)

        for index, card in enumerate(cards):
            print()
            print(f"Card {index + 1}/{total}")
            self.print_card(card.question)

            user_answer = input("Your answer: ")

            if user_answer.strip().lower() == card.answer.strip().lower():
                print("Correct!")
                score += 1
            else:
                print("Wrong!")

            while True:
                print()
                print("1.Show answer")
                print("2.Next card")
                print("3.Back to main menu")

                choice = input("Choose option: ")

                if choice == "1":
                    self.print_card(card.answer)

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