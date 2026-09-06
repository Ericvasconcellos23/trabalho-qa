from pages.login_page import LoginPage
from utils import constantes


def test_checkout_sem_nome(pagina):

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

    # Preencher apenas sobrenome e CEP
    checkout.preencher_sobrenome("Rocha")
    checkout.preencher_cep("26000-000")

    # Tentar continuar sem informar o nome
    checkout.continuar()

    # Validar mensagem de erro
    assert checkout.obter_mensagem_erro() == "Error: First Name is required"

def test_checkout_sem_sobrenome(pagina):

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

    # Preencher apenas nome e CEP
    checkout.preencher_nome("Eric")
    checkout.preencher_cep("26000-000")

    # Tentar continuar sem informar o sobrenome
    checkout.continuar()

    # Validar mensagem de erro
    assert checkout.obter_mensagem_erro() == "Error: Last Name is required"


def test_checkout_sem_cep(pagina):

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

    # Preencher apenas nome e sobrenome
    checkout.preencher_nome("Eric")
    checkout.preencher_sobrenome("Rocha")

    # Tentar continuar sem informar o CEP
    checkout.continuar()

    # Validar mensagem de erro
    assert checkout.obter_mensagem_erro() == "Error: Postal Code is required"