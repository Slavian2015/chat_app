from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from src.handlers.websocket.chats import ChatWebsocketHandler


class HandlersContainer(DeclarativeContainer):
    services = providers.DependenciesContainer()
    get_chat = providers.Factory(ChatWebsocketHandler, websocket_manager=services.websocket_manager)