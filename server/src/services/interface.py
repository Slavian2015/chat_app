from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from fastapi import WebSocket


class WebsocketManagerInterface(ABC):
    @abstractmethod
    async def connect(self, room_id: int, websocket: WebSocket) -> None:
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self, room_id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    async def notify_user(self, user_id: int, message: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_connection(self, room_id: int) -> WebSocket | None:
        raise NotImplementedError
