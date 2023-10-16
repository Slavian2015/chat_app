import time
from faker import Faker
from src.domain.chats import Message


def test_message_creation(faker: Faker) -> None:
    client_id = int(time.time())
    message_sentence = faker.sentence()

    message = Message(client_id=client_id, message=message_sentence)
    assert message.sender == client_id
    assert message.message == message_sentence
