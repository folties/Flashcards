from controller.MainController import MainController
from repository.CardRepository import CardRepository
from service.FileService import FileService


def main():
    card_repository = CardRepository()
    file_service = FileService()
    contoller = MainController(card_repository, file_service)
    contoller.run()

if __name__ == "__main__":
    main()