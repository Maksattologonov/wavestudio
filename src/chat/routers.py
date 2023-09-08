import json
import uuid
from typing import List, Optional, Union
from uuid import UUID

from fastapi import APIRouter, Depends, Response
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from src.chat.models import chat, user_chat
from src.chat.schemas import Chat, UserChatBaseModel
from src.chat.services import ChatService
from src.users.models import user
from src.users.schemas import UserBaseModel

router = APIRouter(
    prefix='/chat',
    tags=['Chat']
)


@router.get('/', response_model=List[Chat])
async def get_chat(session: AsyncSession = Depends(get_async_session)):
    query = select(chat)
    result = await session.execute(query)
    return result.all()


@router.get('/user_chat', response_model=List[UserChatBaseModel])
async def get_sender(user_id: Optional[uuid.UUID] | None = None, session: AsyncSession = Depends(get_async_session)):
    stmt = select(user_chat)
    print(stmt)
    result = await session.execute(stmt)
    return result.all()
