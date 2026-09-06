from pages.login_page import LoginPage
from utils import constantes


def test_checkout(pagina):
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
    checkout.preencher_nome("Eric")
    checkout.preencher_sobrenome("Rocha")
    checkout.preencher_cep("26000-000")

    # Continuar para revisão
    overview = checkout.continuar()

    # Validar página de revisão
    assert overview.verificar_que_esta_no_overview() == "Checkout: Overview"

    # Finalizar compra
    overview.finalizar_compra()
    # Validar Compra finalizada
    assert overview.obter_mensagem_sucesso() == "Thank you for your order!"