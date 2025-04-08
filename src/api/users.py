from fastapi import APIRouter, Depends, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from src.schemas import User
from src.services.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

limiter = Limiter(key_func=get_remote_address)


@router.get(
    "/me", response_model=User, responses={401: {"description": "Unauthorized"}}
)
@limiter.limit("5/minute")
async def me(request: Request, user: User = Depends(get_current_user)):
    return user
