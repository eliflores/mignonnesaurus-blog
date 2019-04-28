from unittest import TestCase
from blog.forms import PostForm, CommentForm


class PostFormTestCase(TestCase):
    def test_form_is_valid_when_both_title_and_text_are_present(self):
        form = PostForm(data={'title': 'test title', 'text': 'test text'})

        self.assertTrue(form.is_valid())


class CommentFormFormTestCase(TestCase):
    def test_form_is_valid_when_both_author_and_text_are_present(self):
        form = CommentForm(data={'author': 'Han Solo', 'text': 'test text'})

        self.assertTrue(form.is_valid())
