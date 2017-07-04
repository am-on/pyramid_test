from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
