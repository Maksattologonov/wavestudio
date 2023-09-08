import uuid as uuid
from typing import Optional

from pydantic import BaseModel, Field


class UserBaseModel(BaseModel):
    uuid: uuid.UUID
    username: str
    photo_url: str = None

    class Config:
        orm_mode = True
