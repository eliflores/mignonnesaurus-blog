import os

from seleniumbase import BaseCase
from seleniumbase.core import browser_launcher

from driver import SeleniumBaseDriver
from page import AdminLoginPage
from page import HomePage
from page import NewCommentPage
from page import NewPostPage
from page import PostPage
from tests.webdriver import get_firefox_binary_or_raise

MY_BLOG_USERNAME = os.getenv('MY_BLOG_USERNAME')
MY_BLOG_PASSWORD = os.getenv('MY_BLOG_PASSWORD')

_original_set_firefox_options = getattr(browser_launcher, "_set_firefox_options")


def _patched_set_firefox_options(*args, **kwargs):
    options = _original_set_firefox_options(*args, **kwargs)
    options.binary_location = get_firefox_binary_or_raise()
    return options


browser_launcher._set_firefox_options = _patched_set_firefox_options


class BlogDemo(BaseCase):
    def setUp(self, masterqa_mode=False):

        super().setUp()
        self.page_driver = SeleniumBaseDriver(self)

    def test_post_interactions(self):
        home_page = HomePage(self.page_driver, self.start_page)
        new_post_page = NewPostPage(self.page_driver)
        post_page = PostPage(self.page_driver)
        new_comment_page = NewCommentPage(self.page_driver)

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
        admin_login_page = AdminLoginPage(self.page_driver,  self.start_page)
        admin_login_page.load()
        admin_login_page.login(MY_BLOG_USERNAME, MY_BLOG_PASSWORD)

