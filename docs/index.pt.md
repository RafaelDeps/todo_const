# Bem-vindo ao todo-const 🚀

Uma aplicação de Lista de Tarefas (TODO) robusta, resiliente e leve, construída com **Python** e **Flask**, seguindo princípios arquiteturais estritos de persistência JSON local e design centrado no usuário.

## 🌟 Funcionalidades Principais

- **CRUD Completo**: Crie, visualize, atualize e exclua tarefas com facilidade.
- **Status da Tarefa**: Alterne entre "Pendente" e "Concluída" com feedback visual imediato.
- **Lembretes Inteligentes**: Defina datas e horários específicos. A aplicação inclui notificações internas (in-app) para manter você no prazo.
- **Portabilidade de Dados**: 
    - **Exportar**: Faça backup de toda a sua lista para um arquivo JSON local.
    - **Importar**: Restaure ou mescle tarefas de um arquivo JSON. A "Mesclagem Inteligente" evita duplicatas verificando títulos e horários.
- **Local-First**: Sem necessidade de banco de dados externo. Tudo é salvo em um arquivo `tasks.json` resiliente.

## 🛠️ Arquitetura

O projeto segue o padrão **MVC (Model-View-Controller)**:
- **Model**: Classes Python puras lidando com I/O JSON atômico e validação.
- **View**: Templates renderizados no servidor usando **Jinja2** e CSS puro.
- **Controller**: Coordenação de rotas e lógica de negócio via **Flask**.

## 🚀 Começando

### Instalação e Execução

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=src.app
flask run
```

## 🧪 Testes e Qualidade

```bash
# Executar testes
PYTHONPATH=. pytest tests/

# Linting e Checagem de Tipos
flake8 src tests
mypy src tests
```
