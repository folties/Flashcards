from model.Card import Card


class MainController:

    def __init__(self, card_service):
        self.card_service = card_service

    def display_menu(self):
        print()
        print("=========Menu=========")
        print("Choose option:")
        print("1.Add new card")
        print("2.Import cards from a file")
        print("3.List all cards")
        print("4.Start a quiz")
        print("5.Exit")

    def run(self):
        running = True

        while running:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                question = input("Enter your question: ")
                answer = input("Enter your answer: ")
                topic = input("Enter your topic: ")

                self.card_service.add_card(question, answer, topic)

                print("Card added")

            elif choice == "2":
                cards = self.file_service.import_cards("cards.txt")
                for card in cards:
                    self.card_repository.add_card(card)


            elif choice == "3":

                cards = self.card_service.get_all_cards()

                if len(cards) == 0:
                    print("\nNo cards added")

                for card in cards:
                    print(card)

            elif choice == "4":
                print("Not implemented yet")

            elif choice == "5":
                print("Program finished")
                running = False