from __future__ import annotations
from pydantic import BaseModel
from src.domain.chats import Message


class MessageResponse(BaseModel):
    sender: str | int
    message: str | None
    datetime: str
    time: str

    @staticmethod
    def from_data(message: Message) -> MessageResponse:
        return MessageResponse(
            sender=message.sender,
            message=message.message,
            datetime=str(message.datetime),
            time=message.time,
        )
