import os
from dotenv import load_dotenv
load_dotenv()

USUARIO_VALIDO = os.getenv("SAUCE_USERNAME")
SENHA_VALIDA = os.getenv("SAUCE_PASSWORD")

URL = "https://www.saucedemo.com/"

PRODUTO_MOCHILA = "Sauce Labs Backpack"