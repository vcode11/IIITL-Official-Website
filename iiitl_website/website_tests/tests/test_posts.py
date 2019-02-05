# -*- coding: utf-8 -*-

import datetime

import django_dynamic_fixture as fixture
from unittest import mock
from django.test import TestCase

from blog.models import Post


class TestPostModel(TestCase):

    """Tests for Post Model."""

    def test_creating_post(self):
        mocked = datetime.datetime.now()
        with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
            self.assertFalse(Post.objects.filter(title='Sample Post Title').exists())
            post = fixture.get(
                Post,
                title='Sample Post Title'
            )

        self.assertEqual(post.date_added, mocked)
        self.assertEqual(str(post), 'Sample Post Title')
        self.assertEqual(post.is_draft, True)
        self.assertEqual(post.is_published, False)
