import uuid

from sqlalchemy import Table, MetaData, Column, Integer, UUID, String, Boolean, SmallInteger, ForeignKey

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('username', String, nullable=False, unique=True),
    Column('photo_url', String, nullable=True),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)



