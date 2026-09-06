import json

from pages.login_page import LoginPage
from utils import constantes


def test_checkout(pagina):

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

    # Adicionar mochila ao carrinho
    produtos.adicionar_mochila()

    # Abrir carrinho
    carrinho = produtos.abrir_carrinho()

    # Ir para checkout
    checkout = carrinho.ir_para_checkout()

    # Preencher dados
    checkout.preencher_nome(cliente["nome"])
    checkout.preencher_sobrenome(cliente["sobrenome"])
    checkout.preencher_cep(cliente["cep"])

    # Continuar para revisão
    overview = checkout.continuar()

    # Validar página de revisão
    assert overview.verificar_que_esta_no_overview() == "Checkout: Overview"

    # Finalizar compra
    overview.finalizar_compra()
    # Validar Compra finalizada
    assert overview.obter_mensagem_sucesso() == "Thank you for your order!"