from playwright.sync_api import Page

class CarrinhoPage:
    def __init__(self, page: Page):
        self.page = page

        self.nome_produto = page.locator(".inventory_item_name")
        self.botao_remover = page.locator("#remove-sauce-labs-backpack")
        self.botao_checkout = page.locator("#checkout")

    def obter_nome_produto(self):
        return self.nome_produto.text_content()

    def produto_esta_visivel(self):
        return self.nome_produto.is_visible()

    def remover_produto(self):
        self.botao_remover.click()

    def ir_para_checkout(self):
         self.botao_checkout.click()