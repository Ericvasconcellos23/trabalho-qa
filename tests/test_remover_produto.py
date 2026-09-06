from pages.login_page import LoginPage
from utils import constantes


def test_remover_produto_do_carrinho(pagina):

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

    # Validar que o produto foi adicionado
    assert carrinho.produto_esta_visivel()
    assert carrinho.quantidade_itens() == 1

    # Remover produto
    carrinho.remover_produto()

    # Validar que o carrinho ficou vazio
    assert carrinho.quantidade_itens() == 0