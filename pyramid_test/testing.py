"""Shared/Common testing code."""
from pyramid_basemodel import Base
from pyramid_basemodel import Session
from sqlalchemy import create_engine
from sqlalchemy.pool import SingletonThreadPool

from pyramid_test.scripts.populate import add_posts


def initTestingDB(
    skip_bind=False,
    posts=False,
    debug_sql=False,
):

    if not skip_bind:
        # Clean registry, since tests don't use forking and
        # db from previous invocation is never removed
        Session.remove()
        engine = create_engine(
            'sqlite:///:memory:', poolclass=SingletonThreadPool,
            isolation_level='SERIALIZABLE', echo=debug_sql
        )
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)
    else:
        Base.metadata.create_all()

    if posts:
        add_posts()
