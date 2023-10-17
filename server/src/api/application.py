from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import src
from src.api.error_handlers import RequireValidationError
from src.api.error_handlers import DomainError
from src.api.error_handlers import http409_error_handler
from src.api.error_handlers import http403_error_handler
from src.services.errors import ServiceError
import src.api.chats.router as chats_endpoints
import src.api.auth.router as auth_endpoints
from src.api.error_handlers import service_error_handler
from src.container import AppContainer

BASE_PATH = Path(__file__).parent.parent.parent.absolute()
load_dotenv(BASE_PATH / '.env')

container = AppContainer()

container.config.base_dir.from_value(BASE_PATH)
container.config.gpt_dir.from_value(BASE_PATH / 'storage')
# CHAT_GPT
container.config.openai_api_sercret.from_env('OPENAI_API_KEY', '')

container.wire(packages=[src])

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=['0.0.0.0', '*', 'localhost', 'http://localhost:3002', 'http://0.0.0.0:3002'],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

api.add_exception_handler(DomainError, http409_error_handler)
api.add_exception_handler(RequireValidationError, http403_error_handler)
api.add_exception_handler(ServiceError, service_error_handler)

api.include_router(auth_endpoints.router, tags=['auth'])
api.include_router(chats_endpoints.router, tags=['chats'])
