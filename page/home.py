from selenium.common.exceptions import NoSuchElementException


class HomePage:
    ADD_LINK = '.glyphicon-plus'
    BLOG_TITLE_LINK = 'link='
    LOGOUT_LINK = 'link=Log out'

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.open(self.base_url)

    def new_post(self):
        self.driver.click(self.ADD_LINK)

    def view_post(self, title):
        self.driver.click(self.BLOG_TITLE_LINK + title)

    def logout(self):
        self.driver.click(self.LOGOUT_LINK)

    def has_post_with_title(self, title):
        try:
            element = self.driver.element_with_text(title)
            return element.is_displayed()
        except NoSuchElementException:
            return False
