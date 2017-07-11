"""Unit test views."""
import unittest

import mock
from pyramid import testing


class ViewPostsTests(unittest.TestCase):
    """Class for unit test views."""

    def setUp(self):
        """Test setup function."""
        self.config = testing.setUp()

    def tearDown(self):
        """Test tear down function."""
        testing.tearDown()

    def test_view_add_form(self):
        """Test add post form."""
        from pyramid_test.views.default import add_post_form

        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        response = add_post_form(request)
        self.assertEqual(response, {})

    @mock.patch('pyramid_test.models.Post.get_all')
    def test_view_index(self, get_all):
        """Test index page."""
        from pyramid_test.models import Post
        from pyramid_test.views.default import index

        request = testing.DummyRequest()
        request.context = testing.DummyResource()

        post = Post(title='title', content='content')
        get_all.return_value = [post, ]

        response = index(request)
        self.assertEqual(response, {'posts': [post, ]})

    @mock.patch('pyramid.request')
    def test_add(self, request):
        """Test adding new post."""
        from pyramid.httpexceptions import HTTPFound
        from pyramid_test.views.default import add_post
        from pyramid_basemodel import Session
        from testing import initTestingDB
        from pyramid_test.models import Post

        initTestingDB(skip_bind=False, posts=False)

        post = Post(id=1, title='post title', content='post content')

        request.params = ({'form.submitted': 'Submit',
                           'title': post.title,
                           'content': post.content,
                           })
        url = '/post/1'
        request.route_url.return_value = url
        expectedResponse = HTTPFound(location=url)

        response = add_post(request)

        added_post = Session.query(Post).first()

        self.assertEqual(post.id, added_post.id)
        self.assertEqual(post.title, added_post.title)
        self.assertEqual(post.content, added_post.content)
        self.assertEqual(response.location, expectedResponse.location)

    @mock.patch('pyramid_test.models.Post.get')
    def test_view_single_post(self, mock):
        """Test single post view."""
        from pyramid_test.models import Post
        from pyramid_test.views.default import single_post

        request = testing.DummyRequest()
        request.context = testing.DummyResource()
        request.matchdict = {'post_id': 1}

        post = Post(title='title', content='content')
        mock.return_value = post

        response = single_post(request)
        self.assertEqual(response, {'post': post})
        print(response)

    @mock.patch('pyramid_test.models.Post.get')
    def test_view_single_post_404(self, mock):
        """Test 404 error on unexisting post."""
        from pyramid.httpexceptions import HTTPNotFound
        from pyramid_test.views.default import single_post

        request = testing.DummyRequest()
        request.context = testing.DummyResource()

        mock.return_value = None

        request.matchdict = {'post_id': 1}

        self.assertRaises(HTTPNotFound, single_post, request)
