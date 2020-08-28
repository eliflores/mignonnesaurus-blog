from selenium.webdriver.common.by import By

from driver.driver import Driver


class SeleniumDriver(Driver):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, selector):
        if self.__is_link_text_selector(selector):
            link_text = self.__get_link_text(selector)
            self.driver.find_element(by=By.LINK_TEXT, value=link_text).click()
        else:
            self.driver.find_element(by=By.CSS_SELECTOR, value=selector).click()

    def type(self, selector, text):
        self.driver.find_element(by=By.CSS_SELECTOR, value=selector).send_keys(text)

    def maximize_window(self):
        self.driver.maximize_window()

    def element_with_text(self, text):
        return self.driver.find_element_by_xpath("//*[contains(text(), '" + text + "')]")

    @staticmethod
    def __is_link_text_selector(selector):
        return selector.startswith('link=')

    @staticmethod
    def __get_link_text(selector):
        return selector.split('link=')[1]
