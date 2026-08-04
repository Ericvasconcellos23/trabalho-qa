from playwright.sync_api import Page
from pages.produtos_page import ProdutosPage
from utils.constantes import URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.usuario = page.locator("#user-name")
        self.senha = page.locator("#password")
        self.botao_entrar = page.locator("#login-button")
        self.mensagem_erro = page.locator("[data-test='error']")

    def acessar(self):
        self.page.goto(URL)
        self.page.wait_for_load_state("networkidle")

    def mensagem_erro_visivel(self):
        return self.mensagem_erro.is_visible()

    def obter_mensagem_erro(self):
        return self.mensagem_erro.text_content()



    def digitar_usuario(self, usuario):
        self.usuario.fill(usuario)

    def digitar_senha (self, senha):
        self.senha.fill(senha)

    def clicar_entrar(self):
        self.botao_entrar.click()
        return ProdutosPage(self.page)


    def fazer_login(self, usuario, senha):
        self.digitar_usuario(usuario)
        self.digitar_senha(senha)
        return self.clicar_entrar()