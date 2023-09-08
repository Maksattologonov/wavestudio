from typing import List, Optional, Union

import uuid
from fastapi import APIRouter, Depends, Query
from pydantic import Field
from sqlalchemy import select, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.users.models import user
from src.users.schemas import UserBaseModel
from src.users.services import UserService

router = APIRouter(
    prefix='/user',
    tags=['User']
)


@router.get('/', response_model=List[UserBaseModel])
async def get_user(user_id: Optional[uuid.UUID] | None = None,
                   username: str | None = None,
                   session: AsyncSession = Depends(get_async_session)):
    if user_id or username:
        stmt = select(user).where(and_(or_(user.c.uuid == user_id, user.c.username == username)))
    else:
        stmt = select(user)
    result = await session.execute(stmt)
    return result.all()
