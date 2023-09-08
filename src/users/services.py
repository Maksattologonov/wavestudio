from fastapi import Depends, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from src.users.models import user


class UserService:
    model = user

    @classmethod
    async def get(cls, session: AsyncSession = Depends(get_async_session), user_id: int = None):
        stmt = select(cls.model).where(cls.model.c.id == user_id)
        result = await session.execute(stmt)
        return result.all()
