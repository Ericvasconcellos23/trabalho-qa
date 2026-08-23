import pytest
import json
import os
from playwright.sync_api import sync_playwright


@pytest.fixture
def pagina(request):

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)

        contexto = navegador.new_context(
            record_video_dir="evidencias/failed"
        )

        pagina = contexto.new_page()

        yield pagina

        nome_teste = request.node.name

        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

            pagina.screenshot(
                path=f"evidencias/failed/{nome_teste}.png",
                full_page=True
            )

            contexto.close()

        else:

            pagina.screenshot(
                path=f"evidencias/passed/{nome_teste}.png",
                full_page=True
            )

            video_path = pagina.video.path()

            contexto.close()

            if os.path.exists(video_path):
                os.remove(video_path)

        navegador.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    resultado = yield

    rep = resultado.get_result()

    if rep.when == "call":
        setattr(item, "rep_call", rep)


@pytest.fixture
def usuario():

    with open("fixtures/usuario.json") as arquivo:
        dados = json.load(arquivo)

    return dados