from starlette.websockets import WebSocket
from starlette.websockets import WebSocketDisconnect
from src.api.chats.response import MessageResponse
from src.command.chats import GetChatCommand
from src.domain.chats import Message
from src.handlers.interface import WebsocketHandlerInterface
from src.services.interface import WebsocketManagerInterface
from src.services.logger import logger


class ChatWebsocketHandler(WebsocketHandlerInterface):
    def __init__(self, websocket_manager: WebsocketManagerInterface) -> None:
        self.websocket_manager = websocket_manager

    async def handle(self, websocket: WebSocket, command: GetChatCommand) -> None:
        try:
            await self.websocket_manager.connect(room_id=command.client_id, websocket=websocket)
            while True:
                data = await websocket.receive_text()

                message = Message(
                    client_id="Server" if data == "Start" else command.client_id,
                    message=data
                )

                logger.info(f"client_id : {'Server' if data == 'Start' else command.client_id}")
                await self.websocket_manager.notify_user(
                    user_id=command.client_id,
                    message=MessageResponse.from_data(message).model_dump()
                )

        except WebSocketDisconnect as e:
            logger.error(f"WebSocketDisconnect :\n{e}")
            await self.websocket_manager.disconnect(room_id=command.client_id)
            return
