class NewPostPage:
    SAVE_POST_BUTTON = '#save-post'
    PUBLISH_POST_BUTTON = '#publish-post'
    TEXT_INPUT = '#id_text'
    TITLE_INPUT = '#id_title'

    def __init__(self, browser):
        self.browser = browser

    def add_post(self, title, text):
        self.browser.type(self.TITLE_INPUT, title)
        self.browser.type(self.TEXT_INPUT, text)
        self.browser.click(self.SAVE_POST_BUTTON)

    def publish_post(self):
        self.browser.click(self.PUBLISH_POST_BUTTON)
