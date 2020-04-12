class PostPage:
    def __init__(self, browser):
        self.browser = browser

    def new_comment(self):
        self.browser.click('.add-comment')

    def delete_post(self):
        self.browser.click('.glyphicon-remove')
