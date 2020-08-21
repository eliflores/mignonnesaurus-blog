from e2e.driver.driver import Driver


class SeleniumBaseDriver(Driver):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.open(url)

    def click(self, selector):
        self.driver.click(selector)

    def type(self, selector, text):
        self.driver.type(selector, text)

    def maximize_window(self):
        self.driver.maximize_window()

    def element_with_text(self, text):
        self.driver.find_element(text)
