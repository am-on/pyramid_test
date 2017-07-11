"""Views for blog."""

from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
from pyramid_basemodel import Session

from pyramid_test.models import Comment
from pyramid_test.models import Post


@view_config(route_name='home', renderer='../templates/posts.pt')
def index(request):
    """Display all blogs."""
    posts = Post.get_all()
    return {'posts': posts}


@view_config(route_name='add',
             request_method='POST',
             request_param='form.submitted',
             )
def add_post(request):
    """Add new post to blog."""
    title = request.params['title']
    content = request.params['content']

    post = Post(title=title, content=content)
    Session.add(post)
    Session.flush()

    next_url = request.route_url('post', post_id=post.id)

    return HTTPFound(location=next_url)


@view_config(route_name='add', renderer='../templates/addpost.pt')
def add_post_form(request):
    """Display form for adding blog posts."""
    return {}


@view_config(route_name='post', renderer='../templates/singlepost.pt')
def single_post(request):
    """Display single post with title, content and comments."""
    post_id = request.matchdict['post_id']
    post = Post.get(post_id)
    if post is None:
        raise HTTPNotFound('No such page')

    return {'post': post}


@view_config(route_name='comment', request_method='POST',
             request_param='form.submitted')
def add_comment(request):
    """Add new comment to blog post."""
    post_id = request.matchdict['post_id']
    post = Post.get(post_id)
    if post is None:
        raise HTTPNotFound('No such page')

    username = request.params['username']
    content = request.params['content']

    comment = Comment(username=username, content=content)
    post.comments.append(comment)

    next_url = request.route_url('post', post_id=post.id)
    return HTTPFound(location=next_url)
