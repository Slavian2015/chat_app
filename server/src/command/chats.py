from pydantic import BaseModel


class GetChatCommand(BaseModel):
    client_id: int
