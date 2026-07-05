# Specification-Driven Development (SpecKit)

This project uses **SpecKit**, a specification-driven development (SDD) methodology that enforces rigorous planning, compliance with a "constitution" of project design rules, and task tracking (including TDD) before any code is written.

## SpecKit Configuration & Structure

The SpecKit automation and metadata are organized into the following components within the repository:

*   **SpecKit Settings:**
    *   `.specify/init-options.json`: Configures global options, including AI integration (`gemini`), sequential branch numbering, and the main context file (`GEMINI.md`).
    *   `.specify/feature.json`: Registers the active feature directory (`specs/001-todo-list-core`).
*   **Project Constitution:**
    *   `.specify/memory/constitution.md` (published at [Project Constitution](constitution.md)): Establishes the **5 non-negotiable principles** that serve as quality gates for any code changes:
        1. **Strictly Python Stack**: Core implementation must be exclusively Python/Flask.
        2. **Local JSON Persistence**: Data persistence must rely solely on local JSON files, strictly prohibiting SQL/NoSQL databases.
        3. **Code Quality & Standards**: Strict compliance with PEP 8, mandatory Type Hints, and snake_case naming conventions.
        4. **Resilience & I/O Integrity**: Robust error handling for all I/O operations to prevent critical crashes.
        5. **User-Centric UX & Error Handling**: Hidden technical stack traces and friendly user-facing messages.
*   **Workflow & Git Automation:**
    *   `.specify/extensions.yml`: Configures Git hooks for automatic feature branch creation (`speckit.git.feature`) and auto-commits (`speckit.git.commit`) before/after each stage.
    *   `.specify/workflows/speckit/workflow.yml`: Defines the complete development pipeline (Full SDD Cycle).
    *   `.gemini/commands/`: Contains custom TOML commands defining step-by-step instructions for the AI during each phase (e.g., `speckit.specify.toml`, `speckit.plan.toml`, `speckit.tasks.toml`, and `speckit.implement.toml`).

---

## Development Cycle and Registered Prompts

The development cycle for the core feature `001-todo-list-core` strictly followed the steps and prompts below:

### 1. Specification (`speckit.specify`)
*   **Input Prompt:** 
    > "Crie a especificação para um TODO List com: 1. CRUD de tarefas (Título/Descrição). 2. Sistema de lembretes por data/hora. 3. Função de Importar/Exportar dados."
*   **Outcome:** Generated the specification document in [Feature Specification](project/001-todo-list-core/spec.md), detailing prioritized user stories (US1, US2, US3) with structured **Given / When / Then** acceptance scenarios, edge cases, and functional requirements.
*   **Quality Gate:** The checklist in `specs/001-todo-list-core/checklists/requirements.md` was used to validate requirement completeness and quality before moving forward.

### 2. Planning (`speckit.plan`)
*   **Input:** The previously generated specification.
*   **Outcome:** Generated the implementation plan in [Implementation Plan](project/001-todo-list-core/plan.md), structuring the MVC architecture, target directories (`src/` and `tests/`), and constitutional check gates.
*   **Additional Context:**
    *   `specs/001-todo-list-core/research.md`: Recorded design choices (e.g., atomic write strategy to guarantee data integrity).
    *   `specs/001-todo-list-core/contracts/api.md`: Documented API/UI route contracts and the JSON import/export schema.

### 3. Task Generation (`speckit.tasks`)
*   **Input:** The design and research documents under `specs/001-todo-list-core/`.
*   **Outcome:** Generated the task list in [Tasks](project/001-todo-list-core/tasks.md), tracking setup, foundational requirements, CRUD, reminders, and export phases formatted as `[ID] [P?] [Story] Description`.

### 4. Implementation (`speckit.implement`)
*   **Input:** The specification, plan, and tasks generated in previous stages.
*   **TDD Enforcement:** As required in the task list, unit and integration tests (e.g., in `tests/unit/test_task_model.py` and `tests/integration/test_crud.py`) were written and verified as failing *before* any implementation logic was written.
