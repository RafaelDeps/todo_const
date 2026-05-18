# Quickstart: TODO List Core Features

**Feature**: [specs/001-todo-list-core/spec.md](spec.md)

## Development Setup

1. **Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run Application**:
   ```bash
   export FLASK_APP=src.app
   export FLASK_DEBUG=1
   flask run
   ```

3. **Verify Installation**:
   Open `http://127.0.0.1:5000` in your browser.

## Key Workflows

### 1. Creating a Task
- Fill the "Title" and optional "Description" on the main page.
- Select an optional reminder date/time.
- Click "Add Task".

### 2. Exporting Data
- Click the "Export" button in the navigation.
- A `tasks.json` file will be downloaded containing all tasks.

### 3. Importing Data
- Click "Import" in the navigation to go to the import page.
- Select a `tasks.json` file.
- Choose "Smart Merge" to safely add new tasks (avoiding exact Title/Reminder duplicates) or "Replace" to clear local data.
- Click "Import".

### 4. Toggling Completion
- Click "Mark Done" on a pending task to complete it (will strike through the title).
- Click "Mark Pending" to un-complete it.

## Testing & Quality

Run the test suite using pytest:
```bash
source venv/bin/activate
PYTHONPATH=. pytest tests/
```

Run static analysis:
```bash
flake8 src tests
mypy src tests
```
