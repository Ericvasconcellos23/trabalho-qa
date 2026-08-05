from pages.login_page import LoginPage
from utils.constantes import PRODUTO_MOCHILA
from utils.constantes import USUARIO_VALIDO, SENHA_VALIDA


def test_adicionar_produto_ao_carrinho(pagina):
    login = LoginPage(pagina)

    login.acessar()
    produtos = login.fazer_login(
        USUARIO_VALIDO,
        SENHA_VALIDA
    )

    produtos.adicionar_mochila()

    carrinho = produtos.abrir_carrinho()

    assert carrinho.produto_esta_visivel()
    assert carrinho.obter_nome_produto() == PRODUTO_MOCHILA
    assert carrinho.quantidade_itens() == 1


    checkout = carrinho.ir_para_checkout()

    checkout.preencher_nome("Eric")
    checkout.preencher_sobrenome("Rocha")
    checkout.preencher_cep("541518544")

    checkout.continuar()
