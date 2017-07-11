"""Comment model definition."""

from pyramid_basemodel import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import func
from sqlalchemy.orm import relationship


class Comment(Base):
    """A class representing Comment model."""

    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False)
    content = Column(Text, nullable=False)
    commented_on = Column(DateTime, default=func.now())
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    post = relationship('Post', backref='comments', cascade='delete,all')
