import os

from django.test import TestCase
from selenium import webdriver

sauce_username = os.environ["SAUCE_USERNAME"]
sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
mignonnesaurus_blog_username = os.environ["MIGNONNESAURUS_BLOG_USERNAME"]
mignonnesaurus_blog_password = os.environ["MIGNONNESAURUS_BLOG_PASSWORD"]
remote_url = "http://ondemand.eu-central-1.saucelabs.com/wd/hub"


class LoginTestCase(TestCase):

    def setUp(self):
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
        self.driver.find_element_by_xpath("//a[@href='/admin/logout/']").click()
        self.driver.quit()

    def test_admin_can_login(self):
        self.driver.get('%s%s' % ('https://mignonnesaurus-staging.herokuapp.com', '/admin/'))
        username_input = self.driver.find_element_by_name('username')
        username_input.send_keys(mignonnesaurus_blog_username)
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(mignonnesaurus_blog_password)
        self.driver.find_element_by_xpath('//input[@value="Log in"]').click()
        self.driver.find_element_by_xpath('//*[contains(text(), "Site administration")]')

        if self.driver.title.startswith('Site administration'):
            self.driver.execute_script('sauce:job-result=passed')
        else:
            self.driver.execute_script('sauce:job-result=failed')
