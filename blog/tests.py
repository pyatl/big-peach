from django.contrib.auth.models import User
from django.test import TestCase

from blog.feeds import LatestEntriesFeed
from blog.models import Post, PostStatus, DRAFT, PUBLISHED


class LatestEntriesFeedTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username='test_user',
            password='123',
            email='test@test.com'
        )
        self.published_post = Post.objects.create(
            title='published title',
            slug='published-title',
            body='published body goes here',
            author=self.test_user,
        )
        self.published_status = PostStatus.objects.create(
            post=self.published_post,
            status=PUBLISHED,
        )
        self.unpublished_post = Post.objects.create(
            title='unpublished title',
            slug='unpublished-title',
            body='unpublished body goes here',
            author=self.test_user,
        )
        self.unpublished_status = PostStatus.objects.create(
            post=self.unpublished_post,
            status=DRAFT,
        )
        self.feed = LatestEntriesFeed()

    def test_entries(self):
        self.assertEqual(
            ['published-title', 'unpublished-title'],
            sorted(p.slug for p in Post.objects.all()),
        )
        self.assertEqual(
            ['published-title'],
            sorted(p.post.slug for p in self.feed.items()),
        )
