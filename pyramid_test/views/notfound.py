"""Page not found view."""


from pyramid.view import notfound_view_config


@notfound_view_config(renderer='../templates/404.pt')
def notfound_view(request):
    """Display 404 template."""
    request.response.status = 404
    return {}
