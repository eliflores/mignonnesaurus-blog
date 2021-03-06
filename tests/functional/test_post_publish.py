from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.webdriver import WebDriver

from driver import SeleniumDriver
from page import AdminLoginPage
from page import HomePage
from page import NewPostPage


class PostPublishTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = options.Options()
        firefox_options.headless = True
        cls.webdriver = WebDriver(options=firefox_options)

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