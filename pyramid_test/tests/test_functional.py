"""Functional tests."""
import unittest

import webtest
from pyramid import testing
from pyramid_basemodel import Session

from pyramid_test import main
from testing import initTestingDB


class FunctionalTests(unittest.TestCase):
    """Class for functional tests."""

    SETTINGS = {
        'sqlalchemy.url': 'sqlite:///:memory:',
    }

    @classmethod
    def setUpClass(self):
        """Class setup method."""
        Session.remove()
        self.config = testing.setUp(settings=self.SETTINGS)

        app = main({}, **self.SETTINGS)
        self.testapp = webtest.TestApp(app)

        initTestingDB(skip_bind=True, posts=True)

    @classmethod
    def tearDownClass(self):
        """Class tear down method."""
        Session.remove()

    def test_index(self):
        """Test index page."""
        res = self.testapp.get('/', status=200)
        self.assertIn(b'Example post title #1', res.body)

    def test_add_post(self):
        """Test if add post form is shown."""
        res = self.testapp.get('/add-post', status=200)
        self.assertIn(b'Add new post', res.body)

    def test_single_post(self):
        """Test single post page."""
        res = self.testapp.get('/post/1', status=200)
        self.assertIn(b'Example post title #1', res.body)
        self.assertIn(b'Joe Doe', res.body)

    def test_post_comment_no_params(self):
        """Test 404 error on visit to post method."""
        res = self.testapp.get('/post/1/comment', status=404)
        self.assertIn(b'Page not found :(', res.body)

    def test_404(self):
        """Test 404 error on visiting unexisting page."""
        res = self.testapp.get('/test-404-page', status=404)
        self.assertIn(b'Page not found :(', res.body)
