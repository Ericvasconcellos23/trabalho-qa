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