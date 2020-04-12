class HomePage:
    ADD_LINK = '.glyphicon-plus'
    BLOG_TITLE_LINK = 'link='
    LOGOUT_LINK = 'link=Log out'
    VIEW_SITE_LINK = 'link=VIEW SITE'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.open(self.browser.start_page)

    def new_post(self):
        self.browser.click(self.ADD_LINK)

    def view_post(self, title):
        self.browser.click(self.BLOG_TITLE_LINK + title)

    def logout(self):
        self.browser.click(self.LOGOUT_LINK)
