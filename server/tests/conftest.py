from typing import Any
from typing import Callable
from typing import Generator

import pytest
from faker import Faker
from starlette.testclient import TestClient

from src.api.application import api
from src.api.application import container
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
