"""Post model definition."""

from pyramid_basemodel import Base
from pyramid_basemodel import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text


class Post(Base):
    """A class representing Post model."""

    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    content = Column(Text, nullable=False)

    @classmethod
    def get_all(cls):
        """Get all posts from databse."""
        posts = Session.query(Post).order_by(Post.id.desc()).all()
        return posts

    @classmethod
    def get(cls, id):
        """Get post with given id."""
        post = Session.query(Post).filter_by(id=id).first()
        return post
