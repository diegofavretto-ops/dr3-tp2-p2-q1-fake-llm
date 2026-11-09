# Parte 2 - Questão 1: Chatbot com Fake LLM

Protótipo de chatbot via FastAPI que utiliza FakeListLLM do LangChain para devolver respostas simuladas a perguntas conhecidas.

Este projeto faz parte do DR3/TP2 da disciplina **Desenvolvimento de Data-Driven Apps com Python**.

## O que foi usado

- **FastAPI** recebe a pergunta.
- **FakeListLLM** pertence ao `langchain-core` e simula uma resposta sem internet e sem custo de tokens.
- Um pequeno dicionário define os assuntos conhecidos.

## 1. Preparar o ambiente

É recomendado utilizar **Python 3.11 ou 3.12**. No terminal, entre na pasta do projeto e execute:

**Windows (PowerShell):**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se `py -3.11` não estiver disponível, utilize `python -m venv .venv` com uma versão compatível.

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2. Executar a API

```bash
uvicorn app:app --reload
```

Depois, acesse a documentação automática do FastAPI: **http://127.0.0.1:8000/docs**.

## 2.1. Exemplo de requisição

**POST** `http://127.0.0.1:8000/chat`

```json
{"pergunta": "O que é FastAPI?"}
```

**Exemplo de resposta:**

```json
{"pergunta": "O que é FastAPI?", "resposta": "FastAPI é um framework Python para criar APIs web.", "simulado": true}
```

Também existe o endpoint **GET** `/assuntos`, que mostra os assuntos previstos. O `FakeListLLM` não gera novas ideias: ele devolve a resposta que configuramos. Isso permite testar rapidamente o fluxo da API.


## 3. Testar

```bash
pytest -q
```

Os testes automatizados usam **simulações (mocks)** para não baixar modelos nem gastar créditos. Para testar o modelo real, execute a aplicação e faça uma requisição pela página `/docs`.

## Observações

O código é um exercício didático. Os modelos locais precisam ser baixados antes da primeira tradução ou geração. A API da OpenAI exige uma chave válida e pode gerar cobrança. O tempo de resposta depende da máquina, do tamanho do texto e da conexão.

**Importante:** as saídas reais não foram inventadas nem medidas. Os testes usam simulações e verificam o processamento do JSON e das rotas.
