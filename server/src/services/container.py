from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from src.services.gpt_manager import GPTManager
from src.services.websockets import ConnectionManager


class ServicesContainer(DeclarativeContainer):
    websocket_manager = providers.Singleton(ConnectionManager)
    gpt_manager = providers.Singleton(GPTManager)
