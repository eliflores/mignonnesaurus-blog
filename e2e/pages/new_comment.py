class NewCommentPage:
    SAVE_COMMENT_BUTTON = '#save-comment'

    def __init__(self, driver):
        self.driver = driver

    def add_comment(self, author, text):
        self.driver.type('#id_author', author)
        self.driver.type('#id_text', text)
        self.driver.click(self.SAVE_COMMENT_BUTTON)
