from playwright.sync_api import Page
from pages.checkout_overview_page import CheckoutOverviewPage

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.campo_nome = page.locator("#first-name")
        self.campo_sobrenome = page.locator("#last-name")
        self.campo_cep = page.locator("#postal-code")



        self.botao_continue = page.locator("#continue")

    def preencher_nome(self, nome):
        self.campo_nome.fill(nome)

    def preencher_sobrenome(self, sobrenome):
        self.campo_sobrenome.fill(sobrenome)

    def preencher_cep(self, cep):
        self.campo_cep.fill(cep)

    def continuar(self):
        self.botao_continue.click()
        return CheckoutOverviewPage(self.page)