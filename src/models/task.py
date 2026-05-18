import json
import os
import tempfile
from typing import List, Dict, Any, Optional, Tuple
from src.utils.helpers import generate_uuid, get_current_iso_time, is_future_date


class TaskModel:
    def __init__(self, db_path: str = "tasks.json"):
        self.db_path = db_path
        self._last_error: Optional[str] = None

    def has_error(self) -> bool:
        return self._last_error is not None

    def get_error(self) -> Optional[str]:
        return self._last_error

    def clear_error(self) -> None:
        self._last_error = None

    def get_all(self) -> List[Dict[str, Any]]:
        self.clear_error()
        if not os.path.exists(self.db_path):
            return []
        if os.path.getsize(self.db_path) == 0:
            return []

        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    self._last_error = "Storage file corrupted (not a list)."
                    return []
                return data
        except json.JSONDecodeError:
            self._last_error = "Storage file corrupted. Could not read tasks."
            return []
        except Exception as e:
            self._last_error = f"Error reading tasks: {str(e)}"
            return []

    def save_all(self, tasks: List[Dict[str, Any]]) -> bool:
        self.clear_error()
        dir_name = os.path.dirname(self.db_path)
        if dir_name and not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name, exist_ok=True)
            except Exception as e:
                self._last_error = f"Could not create directory for tasks: {str(e)}"
                return False

        try:
            fd, temp_path = tempfile.mkstemp(dir=dir_name if dir_name else ".")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(tasks, f, indent=2)

            os.replace(temp_path, self.db_path)
            return True
        except Exception as e:
            self._last_error = f"Failed to save tasks: {str(e)}"
            if "temp_path" in locals() and os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
                except Exception:
                    pass
            return False

    def add_task(
        self, title: str, description: str = "", reminder_at: Optional[str] = None
    ) -> Tuple[bool, Optional[str]]:
        if not title or not title.strip():
            return False, "Title is required."
        if len(title) > 100:
            return False, "Title must be 100 characters or less."

        if reminder_at and not is_future_date(reminder_at):
            return False, "Reminder must be a future date."

        tasks = self.get_all()
        if self.has_error():
            return False, self.get_error()

        new_task = {
            "id": generate_uuid(),
            "title": title.strip(),
            "description": description.strip(),
            "reminder_at": reminder_at,
            "status": "pending",
            "created_at": get_current_iso_time(),
        }

        tasks.append(new_task)
        if self.save_all(tasks):
            return True, None
        return False, self.get_error()

    def update_task(
        self,
        task_id: str,
        title: str,
        description: str = "",
        reminder_at: Optional[str] = None,
    ) -> Tuple[bool, Optional[str]]:
        if not title or not title.strip():
            return False, "Title is required."
        if len(title) > 100:
            return False, "Title must be 100 characters or less."

        if reminder_at and not is_future_date(reminder_at):
            return False, "Reminder must be a future date."

        tasks = self.get_all()
        if self.has_error():
            return False, self.get_error()

        updated = False
        for task in tasks:
            if task["id"] == task_id:
                task["title"] = title.strip()
                task["description"] = description.strip()
                task["reminder_at"] = reminder_at
                updated = True
                break

        if not updated:
            return False, "Task not found."

        if self.save_all(tasks):
            return True, None
        return False, self.get_error()

    def toggle_status(self, task_id: str) -> bool:
        tasks = self.get_all()
        if self.has_error():
            return False

        updated = False
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = (
                    "done" if task.get("status") == "pending" else "pending"
                )
                updated = True
                break

        if not updated:
            return False

        return self.save_all(tasks)

    def delete_task(self, task_id: str) -> bool:
        tasks = self.get_all()
        if self.has_error():
            return False

        original_len = len(tasks)
        tasks = [t for t in tasks if t["id"] != task_id]

        if len(tasks) == original_len:
            return False

        return self.save_all(tasks)

    def import_tasks(
        self, new_tasks: List[Dict[str, Any]], mode: str = "merge"
    ) -> Tuple[bool, Optional[str]]:
        if not isinstance(new_tasks, list):
            return False, "Import data is not a valid list of tasks."

        current_tasks = self.get_all() if mode == "merge" else []
        if self.has_error() and mode == "merge":
            return False, self.get_error()

        if mode == "replace":
            # For replace, we just save the new array
            if self.save_all(new_tasks):
                return True, None
            return False, self.get_error()

        # Smart Merge: Check uniqueness by title and reminder_at
        existing_signatures = set()
        for t in current_tasks:
            title = t.get("title", "")
            rem = t.get("reminder_at") or ""
            existing_signatures.add((title, rem))

        added_count = 0
        for nt in new_tasks:
            title = nt.get("title", "")
            rem = nt.get("reminder_at") or ""
            sig = (title, rem)

            if sig not in existing_signatures:
                # Ensure it has an ID, or generate one
                if "id" not in nt:
                    nt["id"] = generate_uuid()
                current_tasks.append(nt)
                existing_signatures.add(sig)
                added_count += 1

        if self.save_all(current_tasks):
            return True, f"Successfully merged {added_count} new tasks."
        return False, self.get_error()
