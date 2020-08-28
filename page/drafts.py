from selenium.common.exceptions import NoSuchElementException


class DraftsPage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.open(f'{self.base_url}/drafts/')

    def has_post_with_title(self, title):
        try:
            element = self.driver.element_with_text(title)
            return element.is_displayed()
        except NoSuchElementException:
            return False


