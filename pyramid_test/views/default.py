from pyramid.response import Response
from pyramid.view import view_config

from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound

from ..models import Comment
from ..models import Post


@view_config(route_name='home', renderer='../templates/posts.pt')
def my_view(request):
    posts = request.dbsession.query(Post).order_by(Post.id.desc()).all()
    return {'posts': posts}


@view_config(route_name='post', renderer='../templates/singlepost.pt')
def single_post(request):
    post_id = request.matchdict['post_id']
    post = request.dbsession.query(Post).filter_by(id=post_id).first()
    if post is None:
        raise HTTPNotFound('No such page')

    return {'post': post}
