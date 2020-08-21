from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.webdriver import WebDriver

from e2e.driver import SeleniumDriver
from e2e.pages.admin import AdminLoginPage
from e2e.pages.home import HomePage
from e2e.pages.new_post import NewPostPage
from e2e.pages.post import PostPage


class PostDeleteTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = options.Options()
        firefox_options.headless = True
        cls.webdriver = WebDriver(options=firefox_options)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.webdriver.quit()

    def setUp(self):
        self.page_driver = SeleniumDriver(self.webdriver)
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

    def test_a_post_can_be_deleted(self):
        home_page = HomePage(self.page_driver, self.live_server_url)
        new_post_page = NewPostPage(self.page_driver)
        post_page = PostPage(self.page_driver)

        self.login()

        home_page.load()
        home_page.new_post()

        post_title = 'Post Title'
        new_post_page.add_post(post_title, 'Post content')
        new_post_page.publish_post()

        home_page.load()
        home_page.view_post(post_title)

        post_page.delete_post()

        home_page.load()
        self.assertFalse(home_page.has_post_with_title(post_title))

        home_page.logout()

    def login(self):
        admin_login_page = AdminLoginPage(self.page_driver, self.live_server_url)
        admin_login_page.load()
        admin_login_page.login("admin", "password")
