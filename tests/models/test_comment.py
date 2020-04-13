from unittest import TestCase

from blog.models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Post.objects.create(title='Test post', author=user)

    def test_a_comment_is_by_default_not_approved(self):
        post = Post.objects.get(title='Test post')
        comment = Comment.objects.create(post=post)
        self.assertFalse(comment.approved)
