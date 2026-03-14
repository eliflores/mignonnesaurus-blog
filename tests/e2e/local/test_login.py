from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By

from tests.webdriver import create_firefox_webdriver


class LoginTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = create_firefox_webdriver(headless=False)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        logout_buttons = cls.selenium.find_elements(By.XPATH, "//button[normalize-space()='Log out']")
        if logout_buttons:
            logout_buttons[0].click()

        cls.selenium.quit()
        super().tearDownClass()

    def test_admin_can_login(self):
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        username_input = self.selenium.find_element(By.NAME, 'username')
        username_input.send_keys('admin')
        password_input = self.selenium.find_element(By.NAME, 'password')
        password_input.send_keys('password')
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()
        self.selenium.find_element(By.XPATH, '//*[contains(text(), "Site administration")]')

        self.assertTrue(self.selenium.title.startswith('Site administration'))

