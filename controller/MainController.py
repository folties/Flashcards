from exception.InvalidCardDataException import InvalidCardDataException
from util.decorators import menu_action


class MainController:

    def __init__(self, card_service, quiz_service):
        self.card_service = card_service
        self.quiz_service = quiz_service

    def display_menu(self):
        print()
        print("=========Menu=========")
        print("Choose option:")
        print("1.Add new card")
        print("2.Import cards from a JSON file")
        print("3.List all cards")
        print("4.Search cards by topic/category")
        print("5.Start a quiz")
        print("6.Update card")
        print("7.Delete card")
        print("8.Exit")

    def run(self):
        running = True

        while running:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_card()

            elif choice == "2":
                self.import_cards()

            elif choice == "3":
                self.list_cards()

            elif choice == "4":
                self.search_cards()

            elif choice == "5":
                self.quiz_service.start_quiz()

            elif choice == "6":
                self.update_card()

            elif choice == "7":
                self.delete_card()

            elif choice == "8":
                print("Program finished")
                running = False

            else:
                print("Invalid choice")

    @menu_action
    def add_card(self):
        try:
            question = input("Enter your question: ")
            answer = input("Enter your answer: ")
            topic = input("Enter your topic: ")
            category = input("Enter your category: ")

            self.card_service.add_card(question, answer, topic, category)
            print("Card added")

        except InvalidCardDataException as error:
            print(f"Error: {error}")

    @menu_action
    def import_cards(self):
        filename = input("Enter JSON filename: ")

        imported = self.card_service.import_cards_from_file(filename)

        if imported:
            print("Cards imported")
        else:
            print("File is empty or not found")

    @menu_action
    def list_cards(self):
        cards = self.card_service.get_all_cards()

        if len(cards) == 0:
            print("No cards added")
            return

        for index, card in enumerate(cards):
            print(f"{index + 1}. {card}")

    @menu_action
    def search_cards(self):
        topics = self.card_service.get_available_topics()
        if len(topics) > 0:
            print("Available topics: " + ", ".join(topics))

        topic = input("Enter topic: ")

        categories = self.card_service.get_available_categories(topic)
        if len(categories) > 0:
            print("Available categories: " + ", ".join(categories))

        category = input("Enter category or 'all': ")

        cards = self.card_service.find_cards(topic, category)

        if len(cards) == 0:
            print("No cards found")
            return

        for card in cards:
            print(card)

    @menu_action
    def update_card(self):
        cards = self.card_service.get_all_cards()

        if len(cards) == 0:
            print("No cards added")
            return

        for index, card in enumerate(cards):
            print(f"{index + 1}. {card}")

        try:
            number = int(input("Choose card number: "))
            index = number - 1

            question = input("Enter new question: ")
            answer = input("Enter new answer: ")
            topic = input("Enter new topic: ")
            category = input("Enter new category: ")

            updated = self.card_service.update_card(
                index,
                question,
                answer,
                topic,
                category
            )

            if updated:
                print("Card updated")
            else:
                print("Invalid card number")

        except ValueError:
            print("Card number must be an integer")

        except InvalidCardDataException as error:
            print(f"Error: {error}")

    @menu_action
    def delete_card(self):
        cards = self.card_service.get_all_cards()

        if len(cards) == 0:
            print("No cards added")
            return

        for index, card in enumerate(cards):
            print(f"{index + 1}. {card}")

        try:
            number = int(input("Choose card number: "))
            index = number - 1

            deleted = self.card_service.delete_card(index)

            if deleted:
                print("Card deleted")
            else:
                print("Invalid card number")

        except ValueError:
            print("Card number must be an integer")
