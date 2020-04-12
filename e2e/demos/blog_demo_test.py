import os

from seleniumbase import BaseCase

from e2e.pages.admin import AdminPage
from e2e.pages.home import HomePage
from e2e.pages.new_comment import NewCommentPage
from e2e.pages.new_post import NewPostPage
from e2e.pages.post import PostPage

MY_BLOG_USERNAME = os.getenv('MY_BLOG_USERNAME')
MY_BLOG_PASSWORD = os.getenv('MY_BLOG_PASSWORD')


class BlogDemoTest(BaseCase):
    def test_post_interactions(self):
        admin_page = AdminPage(self)
        home_page = HomePage(self)
        new_blog_post_page = NewPostPage(self)
        post_page = PostPage(self)
        new_comment_page = NewCommentPage(self)

        admin_page.load()
        admin_page.login(MY_BLOG_USERNAME, MY_BLOG_PASSWORD)

        home_page.load()
        home_page.new_post()

        new_blog_post_page.add_post('Star Wars IX: The Rise of Skywalker',
                                    'Star Wars IX: The Rise of Skywalker will be released on December 18, 2019.')
        new_blog_post_page.publish_post()

        home_page.load()
        home_page.view_post('Star Wars IX: The Rise of Skywalker')

        post_page.new_comment()
        new_comment_page.add_comment('Yoda', 'Happy I am ❤️')

        post_page.new_comment()
        new_comment_page.add_comment('Han Solo', 'Am I in the movie?')

        post_page.delete_post()

        home_page.load()
        home_page.logout()
