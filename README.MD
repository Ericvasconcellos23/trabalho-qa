# QA Automation Enterprise

Projeto de automação de testes desenvolvido com foco em Qualidade de Software (QA), utilizando Python, Pytest, Playwright e Requests.

O objetivo do projeto é aplicar conceitos utilizados em ambientes reais de QA, incluindo automação de testes Web e API, Page Object Model, cenários positivos e negativos, evidências de execução e relatórios de testes.

## Tecnologias utilizadas

- Python
- Pytest
- Playwright
- Requests
- Allure Report
- python-dotenv
- Git
- GitHub

## Testes Web

A automação Web utiliza o site SauceDemo para validar diferentes fluxos da aplicação.

Entre os cenários automatizados estão:

- Login válido
- Login com usuário inválido
- Login com senha inválida
- Adição de produto ao carrinho
- Remoção de produto do carrinho
- Adição de múltiplos produtos
- Checkout completo
- Checkout sem nome
- Checkout sem sobrenome
- Checkout sem CEP
- Cancelamento do checkout
- Validação do primeiro acesso

A estrutura Web utiliza o padrão Page Object Model (POM), separando a lógica das páginas dos cenários de teste.

## Testes de API

Os testes de API utilizam JSONPlaceholder e Requests.

Foram implementadas validações de:

- GET
- POST
- PUT
- DELETE
- Status codes
- Recurso inexistente (404)
- Estrutura da resposta JSON
- Tipos de dados
- Campos obrigatórios
- Content-Type
- Listagem de usuários
- Tempo de resposta

## Estrutura do projeto

```text
QA_AUTOMATION_ENTERPRISE/
├── api/
│   ├── clients.py
│   └── test_api.py
├── fixtures/
├── pages/
├── tests/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.MD