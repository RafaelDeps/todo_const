# Welcome to todo-const 🚀

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

### Installation & Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=src.app
flask run
```

## 🧪 Testing & Quality

```bash
# Run tests
PYTHONPATH=. pytest tests/

# Linting & Type Checking
flake8 src tests
mypy src tests
```
