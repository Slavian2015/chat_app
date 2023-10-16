from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from src.handlers.container import HandlersContainer
from src.services.container import ServicesContainer


class AppContainer(DeclarativeContainer):
    config = providers.Configuration()
    services = providers.Container(ServicesContainer, open_api_secret=config.open_api_secret)
    handlers = providers.Container(HandlersContainer, services=services)
