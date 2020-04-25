from unittest import TestCase

from blog.models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create(username='testuser')
        Post.objects.create(title='Test post', author=user)

    def test_a_comment_is_by_default_not_approved(self):
        post = Post.objects.get(title='Test post')
        comment = Comment.objects.create(post=post, author="Kenobi", text="Use the Force.")
        self.assertFalse(comment.approved)

    def test_a_comment_can_be_approved(self):
        post = Post.objects.get(title='Test post')
        comment = Comment.objects.create(post=post, author="Vader", text="Join the Dark Side.")
        comment.approve()
        self.assertTrue(comment.approved)
