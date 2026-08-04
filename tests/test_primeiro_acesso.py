from pages.login_page import LoginPage
from utils.constantes import USUARIO_VALIDO, SENHA_VALIDA

def test_primeiro_acesso(pagina):

        login = LoginPage(pagina)

        login.acessar()

        produtos = login.fazer_login(
            USUARIO_VALIDO,
            SENHA_VALIDA

        )

        assert produtos.verificar_que_esta_na_pagina_produtos() == "Products"

