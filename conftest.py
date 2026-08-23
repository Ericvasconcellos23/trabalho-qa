import pytest
import json
import os
import allure
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

            caminho_screenshot = f"evidencias/failed/{nome_teste}.png"

            pagina.screenshot(
                path=caminho_screenshot,
                full_page=True
            )

            allure.attach.file(
                caminho_screenshot,
                name="Screenshot da falha",
                attachment_type=allure.attachment_type.PNG
            )

            video_path = pagina.video.path()

            contexto.close()

            if os.path.exists(video_path):
                allure.attach.file(
                    video_path,
                    name="Video da falha",
                    attachment_type=allure.attachment_type.WEBM
                )

        else:

            caminho_screenshot = f"evidencias/passed/{nome_teste}.png"

            pagina.screenshot(
                path=caminho_screenshot,
                full_page=True
            )

            allure.attach.file(
                caminho_screenshot,
                name="Screenshot do teste",
                attachment_type=allure.attachment_type.PNG
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