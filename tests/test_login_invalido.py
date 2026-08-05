from pages.login_page import LoginPage
from utils.constantes import SENHA_VALIDA, USUARIO_VALIDO


def test_login_com_usuario_invalida(pagina):
    login = LoginPage(pagina)

    login.acessar()

    login.digitar_usuario("usuario_invalido")
    login.digitar_senha(SENHA_VALIDA)

    login.clicar_entrar()

    assert login.mensagem_erro_visivel()

    assert login.obter_mensagem_erro() == (
        "Epic sadface: Username and password do not match any user in this service"
    )


def test_login_com_senha_invalida(pagina):
    login = LoginPage(pagina)

    login.acessar()
    login.digitar_usuario(USUARIO_VALIDO)
    login.digitar_senha("senha_errada")

    login.clicar_entrar()

    assert login.mensagem_erro_visivel()

    assert login.obter_mensagem_erro() == (
        "Epic sadface: Username and password do not match any user in this service"
    )