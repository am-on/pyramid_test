from pyramid.response import Response
from pyramid.view import view_config

from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound

from ..models import Comment
from ..models import Post


@view_config(route_name='home', renderer='../templates/posts.pt')
def index(request):
    posts = request.dbsession.query(Post).order_by(Post.id.desc()).all()
    return {'posts': posts}


@view_config(route_name='add', renderer='../templates/addpost.pt')
def add_post(request):
    if 'form.submitted' in request.params:
        post = Post()
        post.title = request.params['title']
        post.content = request.params['content']
        request.dbsession.add(post)

        request.dbsession.flush()
        next_url = request.route_url('post', post_id=post.id)

        return HTTPFound(location=next_url)

    return {}


@view_config(route_name='post', renderer='../templates/singlepost.pt')
def single_post(request):
    post_id = request.matchdict['post_id']
    post = request.dbsession.query(Post).filter_by(id=post_id).first()
    if post is None:
        raise HTTPNotFound('No such page')

    return {'post': post}


@view_config(route_name='comment')
def add_comment(request):
    post_id = request.matchdict['post_id']
    post = request.dbsession.query(Post).filter_by(id=post_id).first()
    if post is None or 'form.submitted' not in request.params:
        raise HTTPNotFound('No such page')

    username = request.params['username']
    content = request.params['content']

    comment = Comment(username=username, content=content, post_id=post.id)
    post.comments.append(comment)

    next_url = request.route_url('post', post_id=post.id)
    return HTTPFound(location=next_url)
