from controller.MainController import MainController
from repository.CardRepository import CardRepository
from service.CardService import CardService
from service.CardStorageService import CardStorageService
from service.QuizService import QuizService


def main():
    card_repository = CardRepository()
    card_storage_service = CardStorageService()

    card_service = CardService(card_repository, card_storage_service)
    card_service.load_default_cards()

    quiz_service = QuizService(card_service)

    controller = MainController(card_service, quiz_service)

    try:
        controller.run()
    except KeyboardInterrupt:
        print("\nProgram interrupted")


if __name__ == "__main__":
    main()
