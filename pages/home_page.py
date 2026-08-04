from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator(".title")

    def obter_titulo(self):
        return self.page.title()

    def verificar_que_esta_na_home(self):
        return self.titulo.text_content()

