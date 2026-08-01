from playwright.sync_api import Page

class LoginPage(Page):
    def __init__(self, page: Page):
        self.page = page

    def abrir(self):
        self.page.goto("https://www.saucedemo.com/")