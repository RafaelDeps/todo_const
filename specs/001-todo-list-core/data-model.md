# Data Model: TODO List Core Features

**Feature**: [specs/001-todo-list-core/spec.md](spec.md)
**Storage Type**: Local JSON File (`tasks.json`)

## Storage Structure

The system persists all tasks in a single JSON array within `tasks.json`.

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Buy groceries",
    "description": "Milk, eggs, and bread",
    "reminder_at": "2026-05-18T10:00:00Z",
    "status": "pending",
    "created_at": "2026-05-17T14:30:00Z"
  }
]
```

## Entities

### Task

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| `id` | UUID (String) | Unique identifier | Required, Auto-generated |
| `title` | String | Short name of the task | Required, Max 100 chars |
| `description` | String | Detailed information | Optional |
| `reminder_at` | DateTime (ISO 8601) | Scheduled reminder time | Optional, Must be future date |
| `status` | Enum | Completion status | Required, ['pending', 'done'] |
| `created_at` | DateTime (ISO 8601) | Timestamp of creation | Required, Auto-generated |

## State Transitions

- **Pending** → **Done**: Triggered via toggle action in UI.
- **Done** → **Pending**: Triggered via toggle action in UI (unchecking).

## Data Integrity Rules

1. **Uniqueness**: During "Smart Merge", a task is considered a duplicate if its `title` and `reminder_at` match an existing entry exactly.
2. **Resilience**: The `Model` class must wrap JSON `load` and `dump` operations in `try/except` blocks to handle file corruption or permission errors, returning friendly error messages to the Controller.
