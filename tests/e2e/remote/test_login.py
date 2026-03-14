import os

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

remote_url = "http://ondemand.eu-central-1.saucelabs.com/wd/hub"


class LoginTestCase(TestCase):

    def setUp(self):
        sauce_username = os.getenv("SAUCE_USERNAME")
        sauce_access_key = os.getenv("SAUCE_ACCESS_KEY")
        self.blog_username = os.getenv("MIGNONNESAURUS_BLOG_USERNAME")
        self.blog_password = os.getenv("MIGNONNESAURUS_BLOG_PASSWORD")

        if not all([sauce_username, sauce_access_key, self.blog_username, self.blog_password]):
            self.skipTest("Missing Sauce Labs or blog credentials for remote e2e test")

        sauce_options = {
            'screenResolution': '1024x768',
            'seleniumVersion': '3.141.59',
            'build': 'Mignonnesaurus Blog',
            'name': 'login_test_case',
            'username': sauce_username,
            'accessKey': sauce_access_key,
            'tags': ['my_first_blog'],
            'maxDuration': 1800,
            'commandTimeout': 300,
            'idleTimeout': 1000
        }

        firefox_opts = {
            'platformName': 'macOS 10.14',
            'browserName': 'firefox',
            'browserVersion': '67.0',
            'sauce:options': sauce_options
        }
        self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=firefox_opts)

    def tearDown(self):
        logout_buttons = self.driver.find_elements(By.XPATH, "//button[normalize-space()='Log out']")
        if logout_buttons:
            logout_buttons[0].click()

        self.driver.quit()

    def test_admin_can_login(self):
        self.driver.get('%s%s' % ('https://mignonnesaurus-staging.herokuapp.com', '/admin/'))
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.send_keys(self.blog_username)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.blog_password)
        self.driver.find_element(By.XPATH, '//input[@value="Log in"]').click()
        self.driver.find_element(By.XPATH, '//*[contains(text(), "Site administration")]')

        if self.driver.title.startswith('Site administration'):
            self.driver.execute_script('sauce:job-result=passed')
        else:
            self.driver.execute_script('sauce:job-result=failed')

