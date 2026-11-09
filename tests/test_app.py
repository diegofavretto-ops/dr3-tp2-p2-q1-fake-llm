from fastapi.testclient import TestClient

from app import app, escolher_resposta

cliente = TestClient(app)


def test_pergunta_predefinida():
    resposta = cliente.post("/chat", json={"pergunta": "O que é FastAPI?"})
    assert resposta.status_code == 200
    assert "framework Python" in resposta.json()["resposta"]
    assert resposta.json()["simulado"] is True


def test_pergunta_desconhecida():
    assert "não tenho" in escolher_resposta("Qual é a temperatura na Lua?")


def test_entrada_vazia():
    assert cliente.post("/chat", json={"pergunta": " "}).status_code == 422
