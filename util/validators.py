import re
from exception.InvalidCardDataException import InvalidCardDataException


def validate_card_data(question, answer, topic, category):

    values = [question, answer, topic, category]

    if any(value.strip() == "" for value in values):
        raise InvalidCardDataException(
            "Card fields cannot be empty"
        )

    if not re.match(r"^[A-Za-z\s]+$", topic):
        raise InvalidCardDataException(
            "Topic must contain only letters"
        )