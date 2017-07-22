"""Model initializer."""
from sqlalchemy.orm import configure_mappers

# import or define all models here to ensure they are attached to the
# Base.metadata prior to any initialization routines
from .comment import Comment  # noqa
from .post import Post  # noqa

# run configure_mappers after defining all of the models to ensure
# all relationships can be setup
configure_mappers()


def includeme(config):
    """Initialize the model for a Pyramid app.

    Activate this setup using ``config.include('pyramid_test.models')``.
    """
    # use pyramid_tm to hook the transaction lifecycle to the request
    config.include('pyramid_tm')

    config.include('pyramid_basemodel')

    # use pyramid_retry to retry a request when transient exceptions occur
    config.include('pyramid_retry')
