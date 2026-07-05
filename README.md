# todo-const 🚀

A robust, resilient, and lightweight TODO List application built with **Python** and **Flask**, adhering to strict architectural principles of local JSON persistence and user-centric design.

## 🌟 Key Features

- **Full CRUD**: Create, read, update, and delete tasks with ease.
- **Task Status**: Toggle tasks between "Pending" and "Done" with visual feedback.
- **Smart Reminders**: Set specific dates and times for tasks. The application features in-app notifications to keep you on track.
- **Data Portability**: 
    - **Export**: Back up your entire task list to a local JSON file.
    - **Import**: Restore or merge tasks from a JSON file. The "Smart Merge" feature avoids duplicates by checking titles and scheduled times.
- **Local-First**: No external database required. Everything is stored in a resilient local `tasks.json`.

## 🛠️ Architecture

The project follows a clean **MVC (Model-View-Controller)** pattern:
- **Model**: Pure Python classes handling atomic JSON I/O and validation.
- **View**: Server-side rendered templates using **Jinja2** and pure CSS.
- **Controller**: **Flask** routing and business logic coordination.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Virtual environment (recommended)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/RafaelDeps/todo_const.git
    cd todo_const
    ```

2.  **Set up the environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    export FLASK_APP=src.app
    flask run
    ```
    Open `http://127.0.0.1:5000` in your browser.

## 🧪 Testing

The project uses **pytest** for a comprehensive suite of unit and integration tests.

```bash
PYTHONPATH=. pytest tests/
```

## 📜 Documentation

Access the full documentation, including the project constitution and technical specifications, at:
[https://RafaelDeps.github.io/todo_const/](https://RafaelDeps.github.io/todo_const/)

## 🔧 SpecKit: Spec-Driven Development

Este projeto utiliza o **SpecKit**, uma metodologia de desenvolvimento orientada a especificações (*Specification-Driven Development* - SDD) que exige planejamento detalhado, conformidade com uma "constituição" de regras de design do projeto e acompanhamento de tarefas (incluindo TDD) antes do início da escrita de código.

### Configuração e Estrutura do SpecKit

A automação e os metadados do SpecKit estão organizados nos seguintes componentes:

*   **Configurações do SpecKit:**
    *   [.specify/init-options.json](.specify/init-options.json): Configura opções globais, incluindo a integração com a IA (`gemini`), numeração sequencial de branches e o arquivo de contexto principal (`GEMINI.md`).
    *   [.specify/feature.json](.specify/feature.json): Registra o diretório da feature ativa (`specs/001-todo-list-core`).
*   **Constituição do Projeto:**
    *   [.specify/memory/constitution.md](.specify/memory/constitution.md) (com publicação em [docs/constitution.md](docs/constitution.md)): Estabelece os **5 princípios inegociáveis** que servem como portões de qualidade para qualquer alteração no código:
        1. *Strictly Python Stack* (Uso exclusivo de Python/Flask para a lógica principal).
        2. *Local JSON Persistence* (Persistência estritamente em arquivos JSON locais, proibindo bancos SQL/NoSQL).
        3. *Code Quality & Standards* (Adesão estrita ao PEP 8, Type Hints obrigatórios e nomenclatura snake_case).
        4. *Resilience & I/O Integrity* (Tratamento robusto de erros de I/O para evitar falhas críticas).
        5. *User-Centric UX & Error Handling* (Esconder stack traces/erros técnicos e exibir mensagens amigáveis).
*   **Workflow e Automação de Git:**
    *   [.specify/extensions.yml](.specify/extensions.yml): Configura ganchos (hooks) de Git para automação de branches de features (`speckit.git.feature`) e auto-commits (`speckit.git.commit`) antes/depois de cada etapa.
    *   [.specify/workflows/speckit/workflow.yml](.specify/workflows/speckit/workflow.yml): Define a esteira completa do ciclo de desenvolvimento (Full SDD Cycle).
    *   [.gemini/commands/](.gemini/commands/): Contém comandos TOML customizados que definem as instruções passo a passo para a IA em cada fase do ciclo (por exemplo, `speckit.specify.toml`, `speckit.plan.toml`, `speckit.tasks.toml` e `speckit.implement.toml`).

---

### Ciclo de Desenvolvimento e Prompts Registrados

O ciclo de desenvolvimento da feature principal `001-todo-list-core` seguiu rigorosamente os passos e prompts abaixo:

#### 1. Especificação (`speckit.specify`)
*   **Prompt de Entrada:** 
    > "Crie a especificação para um TODO List com: 1. CRUD de tarefas (Título/Descrição). 2. Sistema de lembretes por data/hora. 3. Função de Importar/Exportar dados."
*   **Resultado:** Gerou a especificação em [specs/001-todo-list-core/spec.md](specs/001-todo-list-core/spec.md), detalhando histórias de usuário (US1, US2, US3) com critérios de aceitação estruturados no formato **Given / When / Then**, casos de borda e requisitos funcionais.
*   **Qualidade:** O checklist em [specs/001-todo-list-core/checklists/requirements.md](specs/001-todo-list-core/checklists/requirements.md) foi utilizado para validar a qualidade e completude dos requisitos antes de prosseguir.

#### 2. Planejamento (`speckit.plan`)
*   **Entrada:** A especificação [specs/001-todo-list-core/spec.md](specs/001-todo-list-core/spec.md) gerada anteriormente.
*   **Resultado:** Gerou o plano em [specs/001-todo-list-core/plan.md](specs/001-todo-list-core/plan.md), estruturando a arquitetura técnica (MVC), a árvore de arquivos do projeto (`src/` e `tests/`) e os portões de conformidade constitucional.
*   **Detalhes adicionais:**
    *   [specs/001-todo-list-core/research.md](specs/001-todo-list-core/research.md): Registrou as decisões técnicas do projeto (como escrita atômica para integridade de dados).
    *   [specs/001-todo-list-core/contracts/api.md](specs/001-todo-list-core/contracts/api.md): Documentou os contratos formais das rotas web/SSR e o esquema JSON de persistência/exportação.

#### 3. Tarefas (`speckit.tasks`)
*   **Entrada:** Os documentos de design de `specs/001-todo-list-core/`.
*   **Resultado:** Gerou a lista em [specs/001-todo-list-core/tasks.md](specs/001-todo-list-core/tasks.md), rastreando as etapas de setup, infraestrutura básica, CRUD, lembretes e importação/exportação no formato `[ID] [P?] [Story] Descrição`.

#### 4. Implementação (`speckit.implement`)
*   **Entrada:** A especificação, o plano e as tarefas geradas anteriormente.
*   **Aplicação de TDD:** Conforme exigido no arquivo de tarefas, testes de unidade e integração (ex: em `tests/unit/test_task_model.py` e `tests/integration/test_crud.py`) foram obrigatoriamente escritos e validados (falhando) antes do desenvolvimento da lógica correspondente nos controllers/models.

---

### Documentação Pública (MkDocs)

Todas as especificações, planos e tarefas (incluindo traduções em português `.pt.md`) são compilados de forma unificada usando o **MkDocs** (configurado em [mkdocs.yml](mkdocs.yml)) e expostos no site de documentação oficial do repositório no GitHub Pages.
