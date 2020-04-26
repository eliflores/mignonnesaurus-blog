class AdminLoginPage:
    USERNAME_INPUT = '#id_username'
    PASSWORD_INPUT = '#id_password'
    SUBMIT_BUTTON = 'input[type="submit"]'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.open(f'{self.browser.start_page}/admin/')
        self.browser.maximize_window()

    def login(self, username, password):
        self.browser.type(self.USERNAME_INPUT, username)
        self.browser.type(self.PASSWORD_INPUT, password)
        self.browser.click(self.SUBMIT_BUTTON)
