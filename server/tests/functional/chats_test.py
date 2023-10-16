import time
from typing import Callable
from starlette.testclient import TestClient
from src.domain.chats import Message


def test_chats(
        api_client: TestClient,
        message_factory: Callable[..., Message],
) -> None:
    message = message_factory(client_id=int(time.time()))

    with api_client.websocket_connect(f'/ws/{message.sender}') as websocket:
        websocket.send_text(message.message)
        uploaded_data = websocket.receive_json()
        assert uploaded_data['message'] == message.message
        assert uploaded_data['sender'] == message.sender
