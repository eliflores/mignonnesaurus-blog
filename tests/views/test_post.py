from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post

User = get_user_model()


class PostListViewTest(TestCase):
    def test_uses_post_list_template(self):
        response = self.client.get(f'/')
        self.assertTemplateUsed(response, 'blog/post_list.html')


class PostDetailViewTest(TestCase):
    def test_uses_post_detail_template(self):
        user = User.objects.create(username='testuser')
        post = Post.objects.create(title='Test post', author=user)

        response = self.client.get(f'/post/{post.id}/')
        self.assertTemplateUsed(response, 'blog/post_detail.html')
