from pages.login_page import LoginPage
from utils import constantes


def test_adicionar_multiplos_produtos(pagina):

    login = LoginPage(pagina)

    # Login
    login.acessar()
    produtos = login.fazer_login(
        constantes.USUARIO_VALIDO,
        constantes.SENHA_VALIDA
    )

    # Adicionar dois produtos
    produtos.adicionar_produto("add-to-cart-sauce-labs-backpack")
    produtos.adicionar_produto("add-to-cart-sauce-labs-bike-light")

    # Abrir carrinho
    carrinho = produtos.abrir_carrinho()

    # Validar quantidade
    assert carrinho.quantidade_itens() == 2

    # Validar produtos
    nomes_produtos = carrinho.obter_nomes_produtos()

    assert "Sauce Labs Backpack" in nomes_produtos
    assert "Sauce Labs Bike Light" in nomes_produtos