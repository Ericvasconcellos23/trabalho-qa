from api.clients import ApiClient


def test_buscar_usuario():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/1")

    assert response.status_code == 200

    usuario = response.json()

    assert usuario["id"] == 1
    assert "name" in usuario
    assert "email" in usuario


def test_criar_usuario():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    dados_usuario = {
        "name": "Eric",
        "username": "ericqa",
        "email": "eric@example.com"
    }

    response = client.post("/users", dados_usuario)

    assert response.status_code == 201

    usuario = response.json()

    assert usuario["name"] == "Eric"
    assert usuario["username"] == "ericqa"
    assert usuario["email"] == "eric@example.com"


def test_buscar_usuario_inexistente():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/9999")

    assert response.status_code == 404


def test_validar_campos_usuario():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/1")

    assert response.status_code == 200

    usuario = response.json()

    assert isinstance(usuario["id"], int)
    assert isinstance(usuario["name"], str)
    assert isinstance(usuario["email"], str)
    assert "@" in usuario["email"]


def test_validar_content_type():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/1")

    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

def test_listar_usuarios():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users")

    assert response.status_code == 200

    usuarios = response.json()

    assert isinstance(usuarios, list)
    assert len(usuarios) > 0

def test_usuarios_possuem_campos_obrigatorios():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users")

    assert response.status_code == 200

    usuarios = response.json()

    for usuario in usuarios:
        assert "id" in usuario
        assert "name" in usuario
        assert "username" in usuario
        assert "email" in usuario

def test_atualizar_usuario():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    dados_atualizados = {
        "id": 1,
        "name": "Eric Atualizado",
        "username": "ericqa",
        "email": "eric.atualizado@example.com"
    }

    response = client.put("/users/1", dados_atualizados)

    assert response.status_code == 200

    usuario = response.json()

    assert usuario["name"] == "Eric Atualizado"
    assert usuario["email"] == "eric.atualizado@example.com"

def test_deletar_usuario():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.delete("/users/1")

    assert response.status_code == 200

def test_tempo_resposta_usuario():
    client = ApiClient("https://jsonplaceholder.typicode.com")

    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2