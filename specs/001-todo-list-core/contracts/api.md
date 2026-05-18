# Interface Contracts: TODO List Web UI

**Feature**: [specs/001-todo-list-core/spec.md](../spec.md)
**Type**: Web Application (Flask / Jinja2)

## Web Endpoints (UI Routes)

Since this application uses server-side rendering (SSR) via Flask and Jinja2, the endpoints return HTML responses for GET requests and handle state changes via POST requests.

| Method | Route | Description | Input Parameters |
|--------|-------|-------------|------------------|
| `GET` | `/` | Task List Dashboard | None |
| `POST` | `/tasks/add` | Create a new task | `title`, `description`, `reminder_at` |
| `POST` | `/tasks/<id>/update` | Edit an existing task | `title`, `description`, `reminder_at` |
| `POST` | `/tasks/<id>/toggle` | Toggle completion status | None (ID in URL) |
| `POST` | `/tasks/<id>/delete` | Delete a task | None (ID in URL) |
| `GET` | `/export` | Export tasks to JSON file | Returns `tasks.json` as attachment |
| `POST` | `/import` | Import tasks from JSON | `file` (Multipart), `mode` (Replace/Merge) |

## Data Formats

### Import/Export JSON Schema
Identical to the persistence schema defined in `data-model.md`.

```json
[
  {
    "id": "string",
    "title": "string",
    "description": "string",
    "reminder_at": "ISO8601 string",
    "status": "pending|done"
  }
]
```

## Error Handling Contracts

Internal errors (I/O, validation) are captured by the `Controller` and passed to the `View` as friendly error messages (flashed messages) without exposing stack traces.
