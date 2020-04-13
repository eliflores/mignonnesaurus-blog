from django.test import TestCase

from blog.forms import PostForm


class PostFormTest(TestCase):
    def test_is_valid_when_both_title_and_text_are_present(self):
        form = PostForm(data={'title': 'test title', 'text': 'test text'})

        self.assertTrue(form.is_valid())
