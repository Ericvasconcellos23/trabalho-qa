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

    # Validar quantidade no badge do carrinho
    assert produtos.quantidade_no_badge() == "2"


    # Remover um produto
    produtos.remover_produto("remove-sauce-labs-bike-light")

    # Validar quantidade no badge do carrinho
    assert produtos.quantidade_no_badge() == "1"

    # Abrir carrinho
    carrinho = produtos.abrir_carrinho()

    # Validar quantidade
    assert carrinho.quantidade_itens() == 1

    # Validar produtos
    nomes_produtos = carrinho.obter_nomes_produtos()

    assert "Sauce Labs Backpack" in nomes_produtos
