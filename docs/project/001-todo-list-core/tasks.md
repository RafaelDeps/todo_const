---

description: "Task list for TODO List Core Features implementation"
---

# Tasks: TODO List Core Features

**Input**: Design documents from `/specs/001-todo-list-core/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: TDD approach requested. Tests are mandatory for each functional area.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure (src/, tests/, templates/, static/, utils/) per implementation plan
- [x] T002 Initialize Python project (venv, requirements.txt with Flask, pytest, mypy, flake8)
- [x] T003 [P] Configure Flake8/Black and Mypy for PEP 8 and Type Hint enforcement
- [x] T004 [P] Setup pytest configuration in tests/conftest.py with Flask app fixture

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 [P] Create base CSS layout in src/static/style.css
- [x] T006 [P] Create base Jinja2 template in src/templates/base.html
- [x] T007 [P] Implement helper utilities in src/utils/helpers.py (UUID gen, ISO formatting)
- [x] T008 [P] Write unit tests for JSON I/O resilience in tests/unit/test_task_model.py
- [x] T009 Implement Task Model with atomic JSON I/O and Resilience in src/models/task.py (depends on T008)
- [x] T010 [P] Setup centralized error handling (flashed messages) in src/app.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Task Management (Priority: P1) 🎯 MVP

**Goal**: CRUD operations for tasks (Title/Description/Status)

**Independent Test**: Create, View, Update, Delete a task through the Web UI and verify JSON storage.

### Tests for User Story 1 (TDD)

- [x] T011 [P] [US1] Write unit tests for Task entity validation in tests/unit/test_task_model.py
- [x] T012 [P] [US1] Write integration tests for CRUD routes (/, /tasks/add, /update, /toggle, /delete) in tests/integration/test_crud.py

### Implementation for User Story 1

- [x] T013 [P] [US1] Enhance Task model with validation and status fields in src/models/task.py
- [x] T014 [US1] Implement Main Dashboard route (GET /) in src/app.py
- [x] T015 [US1] Create Index template with task list and add form in src/templates/index.html
- [x] T016 [US1] Implement Create task route (POST /tasks/add) in src/app.py
- [x] T017 [US1] Implement Toggle status route (POST /tasks/<id>/toggle) in src/app.py
- [x] T018 [US1] Implement Update task route (POST /tasks/<id>/update) in src/app.py
- [x] T019 [US1] Implement Delete task route (POST /tasks/<id>/delete) in src/app.py

**Checkpoint**: At this point, User Story 1 is fully functional and testable independently

---

## Phase 4: User Story 2 - Task Reminders (Priority: P2)

**Goal**: System of reminders by date/time

**Independent Test**: Set a reminder for a task and verify it is displayed and triggers a visual notification in the Web UI.

### Tests for User Story 2 (TDD)

- [x] T020 [P] [US2] Write unit tests for reminder date validation in tests/unit/test_task_model.py
- [x] T021 [P] [US2] Write integration tests for reminder display in tests/integration/test_reminders.py

### Implementation for User Story 2

- [x] T022 [P] [US2] Update Task model to handle reminder_at field in src/models/task.py
- [x] T023 [US2] Update Index template to show reminder inputs and display in src/templates/index.html
- [x] T024 [US2] Update Create/Update routes in src/app.py to handle reminder_at
- [x] T025 [US2] Implement In-App visual notification logic (JavaScript) in src/templates/base.html

**Checkpoint**: At this point, User Stories 1 AND 2 are both functional independently

---

## Phase 5: User Story 3 - Data Import/Export (Priority: P3)

**Goal**: Import/Export tasks to/from JSON files

**Independent Test**: Export tasks to a file, clear data, and import the file back choosing "Replace" or "Smart Merge".

### Tests for User Story 3 (TDD)

- [x] T026 [P] [US3] Write unit tests for Smart Merge logic in tests/unit/test_task_model.py
- [x] T027 [P] [US3] Write integration tests for Export/Import routes in tests/integration/test_portability.py

### Implementation for User Story 3

- [x] T028 [P] [US3] Implement Smart Merge and Export logic in src/models/task.py
- [x] T029 [US3] Implement Export route (GET /export) in src/app.py
- [x] T030 [US3] Create Import template with file upload and mode selection in src/templates/import.html
- [x] T031 [US3] Implement Import route (POST /import) in src/app.py

**Checkpoint**: All user stories are now independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and quality checks

- [x] T032 [P] Final PEP 8 linting and Type Hint validation across all files
- [x] T033 [P] Update quickstart.md with final usage examples
- [x] T034 Run full test suite (pytest) to ensure no regressions
- [x] T035 Verify friendly error handling for all I/O failure scenarios

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - US1 (CRUD) is the base for US2 and US3
  - US2 (Reminders) and US3 (Portability) can run in parallel once US1 is stable

### User Story Dependencies

- **User Story 1 (P1)**: Foundation for other stories.
- **User Story 2 (P2)**: Extends US1 models and views.
- **User Story 3 (P3)**: Operates on models established in US1.

### Within Each User Story (TDD Style)

1. Write tests FIRST and ensure they fail.
2. Implement model/service logic.
3. Implement controller/route logic.
4. Implement UI/template logic.
5. Verify tests pass.

---

## Parallel Execution Examples

### Parallel Setup & Foundation

```bash
# Developer A: Setup & Linting
Task: "T002 Initialize Python project"
Task: "T003 Configure Flake8/Black and Mypy"

# Developer B: Infrastructure
Task: "T005 Create base CSS layout"
Task: "T006 Create base Jinja2 template"
```

### Parallel Model & View (Foundational)

```bash
# Parallel execution within Phase 2:
Task: "T008 Write unit tests for JSON I/O resilience" -> "T009 Implement Task Model"
Task: "T007 Implement helper utilities"
Task: "T010 Setup centralized error handling"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL)
3. Complete Phase 3: User Story 1 (CRUD)
4. **STOP and VALIDATE**: Test CRUD independently via Web UI.

### Incremental Delivery

1. Foundation ready.
2. Add CRUD (MVP).
3. Add Reminders.
4. Add Import/Export.
5. Each story is delivered with its own tests.

---

## Notes

- TDD is strictly enforced: Tests (T008, T011, T012, T020, T021, T026, T027) MUST be done before implementation.
- [P] markers indicate tasks with no blocking dependencies within their phase.
- File paths are specific to the requested project structure.
- Resilience and UX principles (from Constitution) are embedded in foundational and story tasks.
