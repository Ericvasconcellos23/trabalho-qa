from playwright.sync_api import Page


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.titulo = page.locator(".title")
        self.nome_produto = page.locator(".inventory_item_name")
        self.botao_finish = page.locator("#finish")
        self.mensagem_sucesso = page.locator(".complete-header")
        self.preco_produto = page.locator(".inventory_item_price")
        self.subtotal = page.locator(".summary_subtotal_label")
        self.taxa = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")

    def verificar_que_esta_no_overview(self):
        return self.titulo.text_content()

    def finalizar_compra(self):
        self.botao_finish.click()

    def obter_mensagem_sucesso(self):
        return self.mensagem_sucesso.text_content()

    def obter_nome_produto(self):
        return self.nome_produto.text_content()

    def obter_preco_produto(self):
        return self.preco_produto.text_content()

    def obter_subtotal(self):
        return self.subtotal.text_content()

    def obter_taxa(self):
        return self.taxa.text_content()

    def obter_total(self):
        return self.total.text_content()