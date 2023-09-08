from datetime import datetime

from sqlalchemy import Table, MetaData, Column, Integer, UUID, String, Boolean, SmallInteger, ForeignKey, DateTime, \
    UniqueConstraint

from src.users.models import user

metadata = MetaData()

chat = Table(
    "chat",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('status', SmallInteger, nullable=False),
    Column('updated_at', SmallInteger, nullable=False)
)

user_chat = Table(
    "user_chat",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('chat_id', Integer, ForeignKey('chat.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey(user.c.uuid), primary_key=True)
)

message = Table(
    'message',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('sender', UUID(as_uuid=True), ForeignKey(user.c.uuid), primary_key=True),
    Column('receiver', UUID(as_uuid=True), ForeignKey(user.c.uuid), primary_key=True),
    Column('text', String, nullable=False),
    Column('time_seen', DateTime),
    Column('time_delivered', DateTime, nullable=False, default=datetime.utcnow),
    Column('is_delivered', Boolean, default=False, nullable=False),
    UniqueConstraint("sender", "receiver", name="unique_user_constraint"),
)
