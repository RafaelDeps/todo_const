# Research: TODO List Core Features

**Feature**: [specs/001-todo-list-core/spec.md](spec.md)

## Implementation Decisions

### Decision 1: Flask for MVC Controller
**Decision**: Use Flask as the primary framework for routing and request handling.
**Rationale**: Flask is lightweight, Python-native, and perfectly suits the MVC pattern without excessive overhead.
**Alternatives considered**: Django (too heavy for a local JSON-based tool), FastAPI (excellent but typically used for JSON APIs, whereas this requires SSR/Jinja2).

### Decision 2: Local JSON I/O Strategy
**Decision**: Use an atomic write pattern (write to temporary file, then rename) to prevent data corruption during crashes.
**Rationale**: Adheres to Principle IV (Resilience). Renaming is generally atomic on modern file systems.
**Alternatives considered**: Direct overwrite (risks file corruption if power/process fails during write).

### Decision 3: "Smart Merge" Logic
**Decision**: Uniqueness determined by `title` and `reminder_at`.
**Rationale**: Prevents common duplicates when users import backups from different times.
**Alternatives considered**: UUID matching (fails if tasks were manually created/duplicated in files).

### Decision 4: In-App Reminders
**Decision**: JavaScript `setTimeout` or `Interval` in the browser will poll or schedule local alerts based on the `reminder_at` fields rendered in the HTML.
**Rationale**: Simplest "Web UI" implementation that doesn't require complex background workers or OS-level integrations.
