import os
import tempfile
import pytest
from src.models.task import TaskModel


@pytest.fixture
def temp_db():
    fd, path = tempfile.mkstemp()
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.unlink(path)


def test_load_non_existent_file(temp_db):
    if os.path.exists(temp_db):
        os.unlink(temp_db)
    model = TaskModel(db_path=temp_db)
    tasks = model.get_all()
    assert tasks == []
    assert not model.has_error()


def test_load_invalid_json(temp_db):
    with open(temp_db, "w") as f:
        f.write("{invalid json")
    model = TaskModel(db_path=temp_db)
    tasks = model.get_all()
    assert tasks == []
    assert model.has_error()
    assert "corrupted" in model.get_error().lower()


def test_save_and_load_tasks(temp_db):
    model = TaskModel(db_path=temp_db)
    task_data = [
        {
            "id": "123",
            "title": "Test Task",
            "description": "Desc",
            "status": "pending",
            "created_at": "2026-05-17T12:00:00Z",
        }
    ]
    success = model.save_all(task_data)
    assert success is True

    tasks = model.get_all()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"


def test_add_valid_task(temp_db):
    model = TaskModel(db_path=temp_db)
    success, error = model.add_task(title="Buy Milk", description="2 liters")
    assert success is True
    assert error is None
    tasks = model.get_all()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Buy Milk"
    assert tasks[0]["status"] == "pending"


def test_add_invalid_task_empty_title(temp_db):
    model = TaskModel(db_path=temp_db)
    success, error = model.add_task(title="", description="")
    assert success is False
    assert "Title is required" in error
    assert len(model.get_all()) == 0


def test_update_task(temp_db):
    model = TaskModel(db_path=temp_db)
    model.add_task(title="Buy Milk")
    task_id = model.get_all()[0]["id"]

    success, error = model.update_task(
        task_id, title="Buy Organic Milk", description="1 liter"
    )
    assert success is True

    tasks = model.get_all()
    assert tasks[0]["title"] == "Buy Organic Milk"
    assert tasks[0]["description"] == "1 liter"


def test_toggle_task_status(temp_db):
    model = TaskModel(db_path=temp_db)
    model.add_task(title="Clean Room")
    task_id = model.get_all()[0]["id"]

    # Toggle to done
    success = model.toggle_status(task_id)
    assert success is True
    assert model.get_all()[0]["status"] == "done"

    # Toggle back to pending
    model.toggle_status(task_id)
    assert model.get_all()[0]["status"] == "pending"


from datetime import datetime, timedelta, timezone


def test_add_task_with_past_reminder(temp_db):
    model = TaskModel(db_path=temp_db)
    past_time = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    success, error = model.add_task(title="Past Reminder", reminder_at=past_time)
    assert success is False
    assert "future date" in error.lower()


def test_add_task_with_future_reminder(temp_db):
    model = TaskModel(db_path=temp_db)
    future_time = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
    success, error = model.add_task(title="Future Reminder", reminder_at=future_time)
    assert success is True
    assert error is None
    tasks = model.get_all()
    assert tasks[0]["reminder_at"] == future_time


def test_import_replace(temp_db):
    model = TaskModel(db_path=temp_db)
    model.add_task(title="Local Task")

    imported_data = [
        {
            "id": "abc",
            "title": "Imported Task",
            "status": "pending",
            "created_at": "2026-05-17T12:00:00Z",
        }
    ]

    success, error = model.import_tasks(imported_data, mode="replace")
    assert success is True

    tasks = model.get_all()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Imported Task"


def test_import_smart_merge(temp_db):
    model = TaskModel(db_path=temp_db)
    model.add_task(title="Local Task", reminder_at="2026-05-20T10:00:00Z")

    imported_data = [
        {
            "id": "abc",
            "title": "Local Task",  # Duplicate
            "reminder_at": "2026-05-20T10:00:00Z",
            "status": "pending",
            "created_at": "2026-05-17T12:00:00Z",
        },
        {
            "id": "def",
            "title": "New Task",  # New
            "status": "done",
            "created_at": "2026-05-17T12:00:00Z",
        },
    ]

    success, error = model.import_tasks(imported_data, mode="merge")
    assert success is True

    tasks = model.get_all()
    assert len(tasks) == 2
    titles = [t["title"] for t in tasks]
    assert "Local Task" in titles
    assert "New Task" in titles
