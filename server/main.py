import logging

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # can alter with time
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, client_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[client_id] = websocket

    def disconnect(self, client_id: int):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def send_personal_message(self, message: dict, client_id: int):
        logger.info(f"active_connection {client_id}\n{message}")
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(json.dumps(message))
        else:
            logger.error(f"active_connection NOT FOUND {client_id}")
            raise Exception("No Connection FOUND")


manager = ConnectionManager()


@app.get("/")
async def get() -> str:
    return "Welcome Home"


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(
        client_id: int,
        websocket: WebSocket,
) -> None:
    await manager.connect(client_id, websocket)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    try:
        while True:
            data = await websocket.receive_text()
            client = "Server" if data == "Start" else client_id
            message = {"time": current_time, "clientId": client, "message": data + "_server"}
            await manager.send_personal_message(message, client_id)

    except WebSocketDisconnect:
        manager.disconnect(client_id)
        message = {"time": current_time, "clientId": client_id, "message": "Offline"}
        logger.error(f"WebSocketDisconnect : {message}")
    except Exception as e:
        logger.error(f"Exception Error :\n{e}")
