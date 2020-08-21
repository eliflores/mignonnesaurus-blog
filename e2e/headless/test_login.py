from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.webdriver import WebDriver

from e2e.driver import SeleniumDriver
from e2e.pages.admin import AdminLoginPage


class LoginTestCase(LiveServerTestCase):
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

    def test_admin_can_login(self):
        admin_login_page = AdminLoginPage(self.page_driver, self.live_server_url)

        admin_login_page.load()
        admin_login_page.login("admin", "password")

        self.assertTrue(self.title().startswith('Site administration'))

        admin_login_page.logout()

    def title(self):
        return self.webdriver.title
