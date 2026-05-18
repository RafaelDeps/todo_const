# todo-const Constitution
<!-- Non-negotiable rules and standards for the todo-const project -->

## Core Principles

### I. Strictly Python Stack
The project must be implemented exclusively using Python. No other programming languages are permitted for core logic or implementation.
**Rationale**: Ensures a consistent development environment, simplifies dependency management, and aligns with the team's expertise.

### II. Local JSON Persistence
Data persistence must rely solely on local JSON files. Use of SQL databases (SQLite, PostgreSQL, etc.) or NoSQL databases (MongoDB, Redis, etc.) is strictly prohibited.
**Rationale**: Prioritizes portability, simplicity, and ease of inspection without requiring external database servers or complex drivers.

### III. Code Quality & Standards
All Python code must adhere to PEP 8 standards. The use of Type Hints is mandatory for all function signatures and public APIs. Naming conventions must strictly follow snake_case.
**Rationale**: Maintains high code readability, ensures type safety during development, and follows idiomatic Python practices.

### IV. Resilience & I/O Integrity
Robust error handling must be implemented for all I/O operations. The application must handle scenarios where files are missing, corrupted, or inaccessible without crashing.
**Rationale**: Guarantees system reliability and prevents data loss or unexpected termination in unstable environments.

### V. User-Centric UX & Error Handling
User-facing messages must be friendly and helpful. Technical error details, stack traces, and internal exceptions must never be displayed to the end-user.
**Rationale**: Provides a professional user experience and prevents exposing internal system details for security and clarity.

## Development Constraints

### Technology Stack & Compliance
- **Primary Language**: Python (strictly)
- **Data Format**: JSON (strictly)
- **Style Guide**: PEP 8
- **Type Safety**: Mandatory Type Hints
- **Naming**: snake_case for all identifiers

## Development Workflow

### Quality Gates
1. **Linting Check**: Must pass PEP 8 compliance.
2. **Type Check**: Must pass static type analysis (e.g., mypy).
3. **Resilience Check**: I/O operations must be wrapped in appropriate try/except blocks with user-friendly error messages.

## Governance
This constitution defines the non-negotiable standards for todo-const. Amendments require documentation and a version bump.

### Amendment Procedure
1. Propose changes in a new version of the constitution.
2. Update dependent templates (`.specify/templates/*`).
3. Ratify the new version and update the `LAST_AMENDED_DATE`.

**Version**: 1.0.0 | **Ratified**: 2026-05-17 | **Last Amended**: 2026-05-17
