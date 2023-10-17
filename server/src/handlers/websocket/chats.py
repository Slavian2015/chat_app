from starlette.websockets import WebSocket
from starlette.websockets import WebSocketDisconnect
from src.api.chats.response import MessageResponse
from src.command.chats import GetChatCommand
from src.domain.chats import Message
from src.handlers.interface import WebsocketHandlerInterface
from src.services.interface import WebsocketManagerInterface
from src.services.interface import GPTInterface
from src.services.logger import logger


class ChatWebsocketHandler(WebsocketHandlerInterface):
    def __init__(self, websocket_manager: WebsocketManagerInterface, gpt_manager: GPTInterface) -> None:
        self.websocket_manager = websocket_manager
        self.gpt_manager = gpt_manager

    async def handle(self, websocket: WebSocket, command: GetChatCommand) -> None:
        try:
            await self.websocket_manager.connect(room_id=command.client_id, websocket=websocket)
            while True:
                user_question = await websocket.receive_text()
                if user_question and user_question != "Start":
                    gpt_result = self.gpt_manager.get_gpt_answer(user_question)
                    logger.error(f"gpt_result :\n{gpt_result}\n\n")
                    gpt_message = Message(client_id="Server", message=gpt_result)
                    await self.websocket_manager.notify_user(
                        user_id=command.client_id,
                        message=MessageResponse.from_data(gpt_message).model_dump()
                    )
        except WebSocketDisconnect as e:
            logger.error(f"WebSocketDisconnect :\n{e}")
            await self.websocket_manager.disconnect(room_id=command.client_id)
