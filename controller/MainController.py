class MainController:

    def __init__(self, card_service, quiz_service):
        self.card_service = card_service
        self.quiz_service = quiz_service

    def display_menu(self):
        print()
        print("=========Menu=========")
        print("Choose option:")
        print("1.Add new card")
        print("2.Import cards from a file")
        print("3.List all cards")
        print("4.Search cards by topic")
        print("5.Start a quiz")
        print("6.Exit")

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
                self.card_service.load_cards_from_file()
                print("Cards imported")

            elif choice == "3":
                cards = self.card_service.get_all_cards()

                if len(cards) == 0:
                    print("\nNo cards added")
                    continue

                for card in cards:
                    print(card)

            elif choice == "4":
                chosen_topic = input("Enter your topic: ")

                cards = self.card_service.find_cards_by_topic(chosen_topic)

                if len(cards) == 0:
                    print("\nNo cards found")
                    continue

                for card in cards:
                    print(card)


            elif choice == "5":
                self.quiz_service.start_quiz()

            elif choice == "6":
                print("Program finished")
                running = False

            else:
                print("Invalid choice")