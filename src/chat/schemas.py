from typing import List, Union
from uuid import UUID

import uuid
from pydantic import BaseModel, Field

from src.users.schemas import UserBaseModel


class Chat(BaseModel):
    id: int
    name: str
    status: int
    updated_at: int

    class Config:
        orm_mode = True


class UserChatBaseModel(BaseModel):
    id: int
    chat_id: Chat
    user_id: UUID

    class Config:
        orm_mode = True
