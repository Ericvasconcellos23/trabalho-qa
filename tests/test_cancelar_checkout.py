import json

from pages.login_page import LoginPage
from utils import constantes


def test_cancelar_checkout(pagina):

    with open("fixtures/checkout.json") as arquivo:
        dados_checkout = json.load(arquivo)

    cliente = dados_checkout["cliente"]

    login = LoginPage(pagina)

    # Login
    login.acessar()
    produtos = login.fazer_login(
        constantes.USUARIO_VALIDO,
        constantes.SENHA_VALIDA
    )

    # Adicionar produto
    produtos.adicionar_mochila()

    # Abrir carrinho
    carrinho = produtos.abrir_carrinho()

    # Ir para checkout
    checkout = carrinho.ir_para_checkout()

    # Preencher dados
    checkout.preencher_nome(cliente["nome"])
    checkout.preencher_sobrenome(cliente["sobrenome"])
    checkout.preencher_cep(cliente["cep"])

    # Cancelar checkout
    checkout.cancelar_checkout()

    # Validar retorno ao carrinho
    assert pagina.locator(".title").text_content() == "Your Cart"