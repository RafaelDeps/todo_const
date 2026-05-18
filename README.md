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
