from unittest import TestCase

from blog.forms import CommentForm


class CommentFormTest(TestCase):
    def test_is_valid_when_both_author_and_text_are_present(self):
        form = CommentForm(data={'author': 'Han Solo', 'text': 'test text'})

        self.assertTrue(form.is_valid())
