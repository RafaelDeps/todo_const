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

This project was built using **SpecKit**, a spec-driven development methodology that enforces rigorous planning before any code is written. Every feature was explicitly defined through formal specification documents before implementation began.

### The SpecKit Process

The development followed a structured workflow documented in `.specify/templates/`:

1. **Specification** (`spec.md`): The feature began with a user description in Portuguese:
   > "Crie a especificação para um TODO List com: 1. CRUD de tarefas (Título/Descrição). 2. Sistema de lembretes por data/hora. 3. Função de Importar/Exportar dados."

2. **User Stories with Acceptance Criteria**: Each user story follows the format defined in `.specify/templates/spec-template.md`:
   - **Given** [initial state], **When** [action], **Then** [expected outcome]
   - Example from `specs/001-todo-list-core/spec.md`:
     > "**Given** an empty task list, **When** I create a task with title "Buy groceries" and description "Milk and eggs", **Then** the task should appear in my list."

3. **Implementation Tasks** (`tasks.md`): Tasks were generated using `.specify/templates/tasks-template.md`, following a TDD approach with phases:
   - **Phase 1**: Setup (venv, requirements.txt)
   - **Phase 2**: Foundational (models, templates, error handling)
   - **Phase 3**: User Story 1 - Task Management (P1 - MVP)
   - **Phase 4**: User Story 2 - Task Reminders (P2)
   - **Phase 5**: User Story 3 - Data Import/Export (P3)

   Each task was tracked with format `[ID] [P?] [Story] Description`, e.g., `T013 [P] [US1] Enhance Task model with validation and status fields`

### Constitution Checks

Before implementation, the system validated against principles defined in `.specify/memory/constitution.md`:

- **Principle I (Strictly Python Stack)**: "The project must be implemented exclusively using Python."
- **Principle II (Local JSON Persistence)**: "Data persistence must rely solely on local JSON files. Use of SQL databases... is strictly prohibited."
- **Principle III (Code Quality & Standards)**: "All Python code must adhere to PEP 8 standards. The use of Type Hints is mandatory..."
- **Principle IV (Resilience & I/O Integrity)**: "Robust error handling must be implemented for all I/O operations..."
- **Principle V (User-Centric UX & Error Handling)**: "User-facing messages must be friendly and helpful. Technical error details... must never be displayed."

These principles were non-negotiable gates that had to pass before each phase could proceed.

### TDD Enforcement

As documented in `specs/001-todo-list-core/tasks.md`:
> "TDD is strictly enforced: Tests (T008, T011, T012, T020, T021, T026, T027) MUST be done before implementation."

Each user story had mandatory test tasks that had to fail before implementation began, ensuring the specification drove the code rather than the other way around.
