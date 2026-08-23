
import pytest
import json
from playwright.sync_api import sync_playwright

@pytest.fixture
def pagina(request):

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        yield pagina

        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
           nome_teste = request.node.name

           pagina.screenshot(
               path=f"evidencias/{nome_teste}.png",
                full_page=True
           )

        navegador.close()

@pytest.hookimpl( hookwrapper=True)
def pytest_runtest_makereport(item, call):

    resultado = yield

    rep = resultado.get_result()

    if rep.when == "call":
        setattr(item,"rep_call", rep)

@pytest.fixture
def usuario():

    with open("fixtures/usuario.json") as arquivo:
        dados = json.load(arquivo)
     
    return dados