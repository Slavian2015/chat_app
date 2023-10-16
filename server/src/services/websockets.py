from starlette.websockets import WebSocket
from src.services.interface import WebsocketManagerInterface


class ConnectionManager(WebsocketManagerInterface):
    def __init__(self) -> None:
        self.rooms: dict[int, WebSocket] = {}

    async def connect(self, room_id: int, websocket: WebSocket) -> None:
        await websocket.accept()
        self.rooms[room_id] = websocket

    async def disconnect(self, room_id: int) -> None:
        del self.rooms[room_id]

    async def notify_user(self, user_id: int, message: dict) -> None:
        connection = self.rooms.get(user_id)
        if connection:
            await connection.send_json(message)

    async def get_connection(self, room_id: int) -> WebSocket | None:
        return self.rooms.get(room_id)
