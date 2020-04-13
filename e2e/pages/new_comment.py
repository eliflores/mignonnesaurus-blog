class NewCommentPage:
    SAVE_COMMENT_BUTTON = '#save-comment'

    def __init__(self, browser):
        self.browser = browser

    def add_comment(self, author, text):
        self.browser.type('#id_author', author)
        self.browser.type('#id_text', text)
        self.browser.click(self.SAVE_COMMENT_BUTTON)
