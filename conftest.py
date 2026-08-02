import pytest
import json
from playwright.sync_api import sync_playwright

@pytest.fixture
def pagina():

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        yield pagina

        navegador.close()

@pytest.fixture
def usuario():

    with open("fixtures/usuarios.json") as arquivo:
        dados = json.load(arquivo)

    return dados
