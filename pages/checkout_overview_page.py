from playwright.sync_api import Page

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator(".title")


    def verifivar_que_esta_no_overwriew(self):
        return self.titulo.text_content() 