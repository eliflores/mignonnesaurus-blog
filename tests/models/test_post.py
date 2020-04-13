from django.test import TestCase
from blog.models import Post
from django.contrib.auth import get_user_model
from freezegun import freeze_time

User = get_user_model()


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_post_does_not_have_a_published_date_by_default(self):
        post = Post.objects.create(title='Test post', author=self.user)

        self.assertIsNone(post.published_date)

    def test_a_publish_post_has_a_published_date(self):
        post = Post.objects.create(title='Test post', author=self.user)

        post.publish()
        self.assertIsNotNone(post.published_date)

    @freeze_time('2019-01-01 00:01:01')
    def test_published_date_is_time_now_by_default(self):
        post = Post.objects.create(title='Test post', author=self.user)

        post.publish()
        self.assertEqual(post.published_date.strftime("%Y-%m-%d %H:%M:%S"), '2019-01-01 00:01:01')
