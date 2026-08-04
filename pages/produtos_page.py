from playwright.sync_api import Page
from pages.carrinho_page import CarrinhoPage


class ProdutosPage:

    def __init__(self, page: Page):
        self.page = page


        self.titulo = page.locator(".title")
        self.botao_mochila = page.locator("#add-to-cart-sauce-labs-backpack")
        self.botao_carrinho = page.locator(".shopping_cart_link")

    def adicionar_mochila(self):
        self.botao_mochila.click()

    def abrir_carrinho(self):
        self.botao_carrinho.click()
        return CarrinhoPage(self.page)

    def verificar_que_esta_na_pagina_produtos(self):
        return self.titulo.text_content()