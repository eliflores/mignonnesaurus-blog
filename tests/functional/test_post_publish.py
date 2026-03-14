from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase

from driver import SeleniumDriver
from page import AdminLoginPage
from page import HomePage
from page import NewPostPage
from tests.webdriver import create_firefox_webdriver


class PostPublishTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.webdriver = create_firefox_webdriver()

    @classmethod
    def tearDownClass(cls):
        cls.webdriver.quit()
        super().tearDownClass()

    def setUp(self):
        self.page_driver = SeleniumDriver(self.webdriver)
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

    def test_a_post_can_be_published(self):
        home_page = HomePage(self.page_driver, self.live_server_url)
        new_post_page = NewPostPage(self.page_driver)

        self.login()

        home_page.load()
        home_page.new_post()

        post_title = 'Post Title'
        new_post_page.add_post(post_title, 'Post content')
        new_post_page.publish_post()

        home_page.load()
        self.assertTrue(home_page.has_post_with_title(post_title))

        home_page.logout()

    def login(self):
        admin_login_page = AdminLoginPage(self.page_driver, self.live_server_url)
        admin_login_page.load()
        admin_login_page.login("admin", "password")
