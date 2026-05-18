# Feature Specification: TODO List Core Features

**Feature Branch**: `001-todo-list-core-001`  
**Created**: 2026-05-17  
**Status**: Draft  
**Input**: User description: "Crie a especificação para um TODO List com: 1. CRUD de tarefas (Título/Descrição). 2. Sistema de lembretes por data/hora. 3. Função de Importar/Exportar dados."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Task Management (Priority: P1)

As a user, I want to create, view, update, and delete tasks so that I can organize my daily activities.

**Why this priority**: Core functionality of the application; without CRUD, other features have no context.

**Independent Test**: Can be tested by creating a task, verifying its presence, updating its content, and finally deleting it.

**Acceptance Scenarios**:

1. **Given** an empty task list, **When** I create a task with title "Buy groceries" and description "Milk and eggs", **Then** the task should appear in my list.
2. **Given** a task "Buy groceries", **When** I update its title to "Buy organic groceries", **Then** the list should reflect the new title.
3. **Given** a task "Buy organic groceries", **When** I delete it, **Then** it should no longer be visible in my list.

---

### User Story 2 - Task Reminders (Priority: P2)

As a user, I want to set a specific date and time for a task reminder so that I don't forget important deadlines.

**Why this priority**: Enhances the utility of the TODO list by adding time-awareness.

**Independent Test**: Can be tested by setting a reminder for a task and verifying that the reminder data is stored and displayed correctly.

**Acceptance Scenarios**:

1. **Given** a task "Doctor appointment", **When** I set a reminder for tomorrow at 10:00 AM, **Then** the task should show the scheduled reminder time.
2. **Given** a task with a reminder, **When** I remove the reminder, **Then** the task should no longer have an associated time.

---

### User Story 3 - Data Import/Export (Priority: P3)

As a user, I want to export my tasks to a file and import them back so that I can backup my data or move it between devices.

**Why this priority**: Provides data portability and resilience against local data loss.

**Independent Test**: Can be tested by exporting a list of tasks, deleting the local data, and then importing the file to restore the list.

**Acceptance Scenarios**:

1. **Given** a list with 5 tasks, **When** I export my data, **Then** a file should be created containing all 5 tasks.
2. **Given** an exported file, **When** I import it into an empty application, **Then** all tasks from the file should be restored with their original titles, descriptions, and reminders.

---

### Edge Cases

- What happens when the JSON storage file is missing or corrupted? (Resilience Principle)
- How does the system handle invalid JSON data during import? (Resilience Principle)
- Are user-facing error messages friendly and non-technical if a reminder date is in the past? (UX Principle)
- What happens if the export location is not writable?

## Clarifications

### Session 2026-05-17
- Q: Should import replace existing data or merge with it? → A: User can choose between Replace and Smart Merge during import.
- Q: What is the primary user interface for this TODO list? → A: Web interface.
- Q: How should the system "remind" the user when the scheduled time is reached? → A: In-app notifications only (visible when the Web UI is open).
- Q: What criteria defines a "duplicate" task during a Smart Merge? → A: Tasks with the same Title AND same Reminder Date/Time.
- Q: Should tasks include a "Completed" status? → A: Yes, tasks can be toggled between Pending and Done.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to create tasks with a mandatory Title and an optional Description.
- **FR-002**: System MUST allow users to retrieve a list of all existing tasks via a Web interface.
- **FR-003**: System MUST allow users to update the Title, Description, Reminder, and Completion Status of an existing task.
- **FR-004**: System MUST allow users to permanently delete a task.
- **FR-005**: System MUST allow users to set a single reminder (date and time) for each task.
- **FR-006**: System MUST export all task data into a JSON file format.
- **FR-007**: System MUST allow users to choose between 'Replace' and 'Smart Merge' when importing a JSON file; duplicates for Smart Merge are identified by matching Title and Reminder Date/Time.
- **FR-008**: System MUST validate that reminder dates are not in the past during creation/update.
- **FR-009**: System MUST provide a browser-based Web UI for all task operations.
- **FR-010**: System MUST display visual notifications for task reminders within the Web UI.
- **FR-011**: System MUST allow users to toggle the completion status of a task (Pending/Done).

### Key Entities

- **Task**: Represents a single item in the TODO list.
  - `title`: String (Required)
  - `description`: String (Optional)
  - `reminder_at`: DateTime (Optional)
  - `status`: Enum (Pending/Done, defaults to Pending)

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of tasks created are successfully persisted to local JSON storage.
- **SC-002**: Users can complete the creation of a task with a reminder in under 15 seconds.
- **SC-003**: Data exported from the system can be validated as standard-compliant JSON.
- **SC-004**: 100% of data integrity is maintained during a full Export-then-Import cycle.
- **SC-005**: Task status toggles are reflected in the Web UI in under 1 second.

## Assumptions

- [Assumption about environment]: The user has local file system write permissions.
- [Assumption about timezones]: All reminders are stored and handled in the system's local timezone.
- [Assumption about storage]: Data is stored in a single `tasks.json` file by default.
