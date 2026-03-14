from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase

from driver import SeleniumDriver
from page import AdminLoginPage
from tests.webdriver import create_firefox_webdriver


class LoginTestCase(LiveServerTestCase):
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

    def test_admin_can_login(self):
        admin_login_page = AdminLoginPage(self.page_driver, self.live_server_url)

        admin_login_page.load()
        admin_login_page.login("admin", "password")

        self.assertTrue(self.title().startswith('Site administration'))

        admin_login_page.logout()

    def title(self):
        return self.webdriver.title
