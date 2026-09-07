from playwright.sync_api import Page
from pages.checkout_overview_page import CheckoutOverviewPage

class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        # Campos do formulário de checkout
        self.campo_nome = page.locator("#first-name")
        self.campo_sobrenome = page.locator("#last-name")
        self.campo_cep = page.locator("#postal-code")
      
        # Mensagem de erro
        self.mensagem_erro = page.locator("[data-test='error']")

        # Botões
        self.botao_continue = page.locator("#continue")
        self.botao_cancelar = page.locator("#cancel")

    def preencher_nome(self, nome):
        self.campo_nome.fill(nome)

    def preencher_sobrenome(self, sobrenome):
        self.campo_sobrenome.fill(sobrenome)

    def preencher_cep(self, cep):
        self.campo_cep.fill(cep)

    def obter_mensagem_erro(self):
        return self.mensagem_erro.text_content()

    def continuar(self):
        self.botao_continue.click()
        return CheckoutOverviewPage(self.page)

    def cancelar_checkout(self):
        self.botao_cancelar.click()
    