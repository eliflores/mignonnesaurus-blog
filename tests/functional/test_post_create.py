from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase

from driver import SeleniumDriver
from page import AdminLoginPage
from page import DraftsPage
from page import HomePage
from page import NewPostPage
from tests.webdriver import create_firefox_webdriver


class PostCreateTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.webdriver = create_firefox_webdriver()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.webdriver.quit()

    def setUp(self):
        self.page_driver = SeleniumDriver(self.webdriver)
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

    def test_a_post_can_be_created(self):
        home_page = HomePage(self.page_driver, self.live_server_url)
        new_post_page = NewPostPage(self.page_driver)
        drafts_page = DraftsPage(self.page_driver, self.live_server_url)

        self.login()

        home_page.load()
        home_page.new_post()

        post_title = 'Post Title'
        new_post_page.add_post(post_title, 'Post content')

        self.assertTrue(drafts_page.has_post_with_title(post_title))

        home_page.logout()

    def login(self):
        admin_login_page = AdminLoginPage(self.page_driver, self.live_server_url)
        admin_login_page.load()
        admin_login_page.login("admin", "password")
