class NewPostPage:
    SAVE_POST_BUTTON = '#save-post'
    PUBLISH_POST_BUTTON = '#publish-post'
    TEXT_INPUT = '#id_text'
    TITLE_INPUT = '#id_title'

    def __init__(self, driver):
        self.driver = driver

    def add_post(self, title, text):
        self.driver.type(self.TITLE_INPUT, title)
        self.driver.type(self.TEXT_INPUT, text)
        self.driver.click(self.SAVE_POST_BUTTON)

    def publish_post(self):
        self.driver.click(self.PUBLISH_POST_BUTTON)
