from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from src.services.websockets import ConnectionManager


class ServicesContainer(DeclarativeContainer):
    open_api_secret = providers.Dependency(instance_of=str)
    websocket_manager = providers.Singleton(ConnectionManager)
