from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from starlette.responses import JSONResponse

from src.services.errors import ServiceError


class DomainError(RuntimeError):
    pass


class RequireValidationError(RuntimeError):
    pass


async def http409_error_handler(_: Request, exc: DomainError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=jsonable_encoder({'detail': {'error': str(exc)}})
    )


async def http403_error_handler(_: Request, exc: RequireValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=jsonable_encoder({'detail': {'error': str(exc)}})
    )


async def service_error_handler(_: Request, exc: ServiceError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({'detail': {'error': str(exc)}})
    )
