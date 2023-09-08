from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.chat.models import chat


class ChatService:
    model = chat

    @classmethod
    async def get(cls, session: AsyncSession):
        query = select(cls.model)
        result = await session.execute(query)
        return result.all()
