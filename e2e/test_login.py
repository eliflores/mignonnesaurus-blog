from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth import get_user_model


class LoginTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_admin_can_login(self):
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('admin')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('password')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.selenium.find_element_by_xpath('//*[contains(text(), "Site administration")]')
