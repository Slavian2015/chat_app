from fastapi import APIRouter
from src.api.auth.response import GeneralSuccessResponse

router = APIRouter()


@router.get('/', response_model=GeneralSuccessResponse)
async def check_status() -> GeneralSuccessResponse:
    return GeneralSuccessResponse()
