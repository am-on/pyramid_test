"""Populate db with dummy data."""

import os
import sys

import transaction
from pyramid.paster import get_appsettings
from pyramid.paster import setup_logging
from pyramid.scripts.common import parse_vars
from pyramid_basemodel import Base
from pyramid_basemodel import Session
from pyramid_basemodel import bind_engine

from pyramid_test.models import Comment
from pyramid_test.models import Post
from pyramid_test.models import get_engine


lorem = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
    do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
    ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
    in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
    officia deserunt mollit anim id est laborum."""


def add_comments(posts):
    """Add comments to posts in given list."""
    users = ['Joe Doe', 'Bob', 'Peter', 'Marry', ]
    short_lorem = lorem[:200]

    for post in posts:
        for user in users:
            comment = Comment(username=user, content=short_lorem)
            post.comments.append(comment)


def add_posts(comments=True):
    """Add example posts with comments."""
    title = 'Example post title #{}'
    posts = []

    with transaction.manager:
        for i in range(1, 5):
            post = Post(title=title.format(i), content=lorem)
            posts.append(post)
        Session.add_all(posts)

        if comments:
            add_comments(posts)

        Session.flush()


def usage(argv):
    """Print usage instructions."""
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    """Populate db."""
    if len(argv) < 2:
        usage(argv)

    config_uri = argv[1]
    setup_logging(config_uri)
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    bind_engine(engine)
    Base.metadata.create_all(engine)

    add_posts(comments=True)


if __name__ == '__main__':
    main()
