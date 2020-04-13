import os

from seleniumbase import BaseCase

from e2e.pages.admin import AdminLoginPage
from e2e.pages.home import HomePage
from e2e.pages.new_comment import NewCommentPage
from e2e.pages.new_post import NewPostPage
from e2e.pages.post import PostPage

MY_BLOG_USERNAME = os.getenv('MY_BLOG_USERNAME')
MY_BLOG_PASSWORD = os.getenv('MY_BLOG_PASSWORD')


class BlogDemoTest(BaseCase):
    def test_post_interactions(self):
        home_page = HomePage(self)
        new_post_page = NewPostPage(self)
        post_page = PostPage(self)
        new_comment_page = NewCommentPage(self)

        self.login()

        home_page.load()
        home_page.new_post()

        new_post_page.add_post('Your Favorite Star Wars Quotes',
                               'What are your favorite Star Wars Quotes?')
        new_post_page.publish_post()

        home_page.load()
        home_page.view_post('Your Favorite Star Wars Quotes')

        post_page.new_comment()
        new_comment_page.add_comment('Han Solo',
                                     '"Crazy thing is, it’s true. The Force, the Jedi — all of it. It’s all true."️')
        post_page.approve_comment()

        post_page.new_comment()
        new_comment_page.add_comment('Yoda', '"Do. Or do not. There is no try."')
        post_page.approve_comment()

        post_page.new_comment()
        new_comment_page.add_comment('Darth Vader', '"I find your lack of faith disturbing."')
        post_page.approve_comment()

        post_page.delete_post()

        home_page.logout()

    def login(self):
        admin_login_page = AdminLoginPage(self)
        admin_login_page.load()
        admin_login_page.login(MY_BLOG_USERNAME, MY_BLOG_PASSWORD)
