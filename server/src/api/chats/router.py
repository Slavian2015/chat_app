from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Depends
from starlette.websockets import WebSocket

from src.command.chats import GetChatCommand
from src.container import AppContainer
from src.handlers.interface import WebsocketHandlerInterface

router = APIRouter()


@router.websocket('/ws/{client_id}')
@inject
async def ws_chat(
        websocket: WebSocket,
        client_id: int,
        handler: WebsocketHandlerInterface = Depends(Provide[AppContainer.handlers.get_chat]),
) -> None:
    command: GetChatCommand = GetChatCommand(client_id=client_id)
    return await handler.handle(websocket=websocket, command=command)
