from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator(".title")
        self.nome_produto = page.locator(".inventory_item_name")
        self.botao_finish = page.locator("#finish")
        self.mensagem_sucesso = page.locator(".complete-header")

    def verificar_que_esta_no_overview(self):
        return self.titulo.text_content()

    def finalizar_compra(self):
        self.botao_finish.click()

    def obter_mensagem_sucesso(self):
        return self.mensagem_sucesso.text_content()

    def obter_nome_produto(self):
        return self.nome_produto.text_content()