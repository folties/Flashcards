from controller.MainController import MainController
from repository.CardRepository import CardRepository
from service.CardService import CardService
from service.FileService import FileService
from service.QuizService import QuizService


def main():
    card_repository = CardRepository()
    file_service = FileService()
    card_service = CardService(card_repository, file_service)
    quiz_service = QuizService(card_service)

    controller = MainController(card_service, quiz_service)
    controller.run()


if __name__ == "__main__":
    main()