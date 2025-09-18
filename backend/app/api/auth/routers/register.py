from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.auth.schemas import UserCreate, UserRegResponse
from app.api.auth.utils import get_password_hash
from app.database.adapter import adapter
from app.database.models import User
from app.database.session import get_async_session
from app.core.logging import get_logger

logger = get_logger()

router = APIRouter()


@router.post("/register", status_code=status.HTTP_200_OK, response_model=UserRegResponse)
async def register(
    user: UserCreate,
    session: Annotated[AsyncSession, Depends(get_async_session)],
):
    username_check = await adapter.get_by_value(User, "username", user.username, session=session)
    if username_check:
        raise HTTPException(409, "Username already exists")
    hash_pwd = get_password_hash(user.password)
    new_user = await adapter.insert(
        User,
        {
            "name": user.name,
            "username": user.username,
            "hashed_password": hash_pwd,
        }
    )
    return UserRegResponse(id=new_user.id)
