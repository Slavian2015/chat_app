from typing import Any
from typing import Callable
from typing import Generator
from unittest.mock import MagicMock

import pytest
from faker import Faker
from pytest_mock import MockFixture
from starlette.testclient import TestClient

from src.api.application import api
from src.api.application import container
from src.container import AppContainer
from src.domain.chats import Message


@pytest.fixture(scope='module')
def app_container() -> Generator:
    yield container


@pytest.fixture
def api_client() -> TestClient:
    return TestClient(api)


@pytest.fixture
def message_factory(faker: Faker) -> Callable[..., Message]:
    def maker(client_id: int | str = "Server", **kwargs: Any) -> Message:
        message = Message(client_id=client_id, message=faker.sentence())
        return message

    return maker


@pytest.fixture
def gpt_manager_factory(
        app_container: AppContainer,
        mocker: MockFixture,
        faker: Faker
) -> Callable[..., MagicMock]:
    def maker(**kwargs: Any) -> MagicMock:
        gpt_manager = mocker.patch('src.services.gpt_manager.GPTManager')
        gpt_manager.get_gpt_answer.return_value = kwargs.get('message', faker.sentence())
        return gpt_manager

    return maker
