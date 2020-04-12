class NewPostPage:
    SAVE_BUTTON = 'button[type="submit"].save'
    TEXT_INPUT = '#id_text'
    TITLE_INPUT = '#id_title'

    def __init__(self, browser):
        self.browser = browser

    def add_post(self, title, text):
        self.browser.type(self.TITLE_INPUT, title)
        self.browser.type(self.TEXT_INPUT, text)
        self.browser.click(self.SAVE_BUTTON)

    def publish_post(self):
        self.browser.click('.publish')
