"""Routes."""


def includeme(config):
    """Config routes for app."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('comment', '/post/{post_id}/comment')
    config.add_route('post', '/post/{post_id}')
    config.add_route('add', '/add-post')
