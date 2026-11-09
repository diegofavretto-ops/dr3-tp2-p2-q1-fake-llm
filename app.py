"""Chatbot simulado usando o FakeListLLM do LangChain."""
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from langchain_core.language_models.fake import FakeListLLM

app = FastAPI(title="Chatbot Fake LLM", version="1.0")

# Respostas predefinidas, sem chamar uma API externa.
PERGUNTAS = {
    "fastapi": "FastAPI é um framework Python para criar APIs web.",
    "langchain": "LangChain ajuda a integrar modelos de linguagem em aplicativos.",
    "python": "Python é uma linguagem de programação muito usada em dados.",
    "oi": "Olá! Você pode perguntar sobre Python, FastAPI ou LangChain.",
    "olá": "Olá! Você pode perguntar sobre Python, FastAPI ou LangChain.",
}


class Entrada(BaseModel):
    pergunta: str = Field(min_length=1, max_length=500)

    @field_validator("pergunta")
    @classmethod
    def validar_pergunta(cls, valor: str) -> str:
        if not valor.strip():
            raise ValueError("A pergunta não pode ficar vazia.")
        return valor.strip()


def escolher_resposta(pergunta: str) -> str:
    pergunta = pergunta.lower()
    for palavra, resposta in PERGUNTAS.items():
        if palavra in pergunta:
            return resposta
    return "Ainda não tenho uma resposta preparada para essa pergunta."


@app.get("/")
def inicio():
    return {"mensagem": "Use POST /chat para conversar com o Fake LLM."}


@app.get("/assuntos")
def assuntos():
    return {"assuntos": ["Python", "FastAPI", "LangChain", "Olá"]}


@app.post("/chat")
def conversar(entrada: Entrada):
    resposta_predefinida = escolher_resposta(entrada.pergunta)
    llm_falso = FakeListLLM(responses=[resposta_predefinida])
    resposta = llm_falso.invoke(entrada.pergunta)
    return {"pergunta": entrada.pergunta, "resposta": resposta, "simulado": True}
