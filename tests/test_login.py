from pages.login_page import LoginPage
from utils import constantes


def test_login_valido(pagina):
    login = LoginPage(pagina)

    login.acessar()
    produtos = login.fazer_login(
        constantes.USUARIO_VALIDO,
        constantes.SENHA_VALIDA
    )

    assert produtos.verificar_que_esta_na_pagina_produtos() == "Products"