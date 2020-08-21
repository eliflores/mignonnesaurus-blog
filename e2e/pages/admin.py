class AdminLoginPage:
    USERNAME_INPUT = '#id_username'
    PASSWORD_INPUT = '#id_password'
    SUBMIT_BUTTON = 'input[type="submit"]'
    LOGOUT_LINK = 'link=LOG OUT'

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def load(self):
        self.driver.open(f'{self.base_url}/admin/')
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.type(self.USERNAME_INPUT, username)
        self.driver.type(self.PASSWORD_INPUT, password)
        self.driver.click(self.SUBMIT_BUTTON)

    def logout(self):
        self.driver.click(self.LOGOUT_LINK)
