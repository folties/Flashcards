# Flashcards

This is a simple Python command line project for creating and using flashcards.
The program stores cards in a JSON file and allows the user to practice them in
quiz mode.

Each card has:

- question
- answer
- topic
- category

## Features

- add new cards
- list all cards
- search cards by topic and category
- start a quiz
- update cards
- delete cards
- import cards from a JSON file

## How To Run

Run the project from the main folder:

```bash
python main.py
```

Then choose an option from the menu.

## Data

Cards are saved in:

```text
data/cards.json
```

Example card:

```json
{
    "question": "Dog",
    "answer": "Perro",
    "topic": "Spanish",
    "category": "animals"
}
```

## Project Structure

- `main.py` - starts the program
- `model/Card.py` - flashcard class
- `controller/MainController.py` - menu and user input
- `service/CardService.py` - main card logic
- `service/CardStorageService.py` - loading and saving JSON
- `service/QuizService.py` - quiz mode
- `repository/CardRepository.py` - stores cards in memory
- `util/validators.py` - validates input
- `util/decorators.py` - custom menu decorator
- `exception/InvalidCardDataException.py` - custom exception

## Python Elements

The project uses classes, functions, lambda, custom decorator, lists,
dictionaries, sets, comprehensions, generator, files with `with`, JSON
serialization, regex, and custom exception handling.
