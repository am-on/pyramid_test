from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    func,
)

from .meta import Base
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    commented_on = Column(DateTime, default=func.now())
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship('Post', backref='comments', cascade='delete,all')
