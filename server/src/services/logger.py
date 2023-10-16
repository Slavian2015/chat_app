import logging
from logging.config import dictConfig
from logging import INFO
from logging import getLevelName
from pydantic.v1 import BaseSettings


class LoggerConfig(BaseSettings):
    LOGGER_NAME: str = "chat_gpt"
    LOG_FORMAT: str = "%(levelprefix)s %(asctime)s %(message)s"
    LOG_LEVEL: str = getLevelName(INFO)

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
        },
    }
    loggers = {
        LOGGER_NAME: {"handlers": ["default"], "level": LOG_LEVEL},
    }



dictConfig(LoggerConfig().dict())
logger = logging.getLogger(LoggerConfig().LOGGER_NAME)
