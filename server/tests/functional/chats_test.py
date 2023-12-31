import time
from typing import Callable
from unittest.mock import MagicMock

from starlette.testclient import TestClient

from src.container import AppContainer
from src.domain.chats import Message


def test_chats(
        app_container: AppContainer,
        api_client: TestClient,
        message_factory: Callable[..., Message],
        gpt_manager_factory: Callable[..., MagicMock],
) -> None:
    message = message_factory(client_id=int(time.time()))

    gpt_manager = gpt_manager_factory(message=message.message)

    with app_container.services.gpt_manager.override(gpt_manager):
        with api_client.websocket_connect(f'/ws/{message.sender}') as websocket:
            websocket.send_text(message.message)
            uploaded_data = websocket.receive_json()
            assert uploaded_data['message'] == message.message
            assert uploaded_data['sender'] == 'Server'
