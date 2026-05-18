import os
from typing import Any, Dict, Optional, Union
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.wrappers import Response
from src.models.task import TaskModel

def create_app(test_config: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    # Simple secret key for flashes
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "tasks.json"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index() -> str:
        model = TaskModel(app.config["DATABASE"])
        tasks = model.get_all()
        if model.has_error():
            flash(model.get_error() or "Unknown error", "error")
        return render_template("index.html", tasks=tasks)

    @app.route("/tasks/add", methods=["POST"])
    def add_task() -> Response:
        title = request.form.get("title", "")
        description = request.form.get("description", "")
        reminder_at = request.form.get("reminder_at") or None

        model = TaskModel(app.config["DATABASE"])
        success, error = model.add_task(title, description, reminder_at)

        if success:
            flash("Task added successfully.", "success")
        else:
            flash(f"Error adding task: {error}", "error")

        return redirect(url_for("index"))

    @app.route("/tasks/<task_id>/update", methods=["POST"])
    def update_task(task_id: str) -> Response:
        title = request.form.get("title", "")
        description = request.form.get("description", "")
        reminder_at = request.form.get("reminder_at") or None

        model = TaskModel(app.config["DATABASE"])
        success, error = model.update_task(task_id, title, description, reminder_at)

        if success:
            flash("Task updated successfully.", "success")
        else:
            flash(f"Error updating task: {error}", "error")

        return redirect(url_for("index"))

    @app.route("/tasks/<task_id>/toggle", methods=["POST"])
    def toggle_task(task_id: str) -> Response:
        model = TaskModel(app.config["DATABASE"])
        if model.toggle_status(task_id):
            flash("Task status updated.", "success")
        else:
            flash("Error updating task status.", "error")
        return redirect(url_for("index"))

    @app.route("/tasks/<task_id>/delete", methods=["POST"])
    def delete_task(task_id: str) -> Response:
        model = TaskModel(app.config["DATABASE"])
        if model.delete_task(task_id):
            flash("Task deleted.", "success")
        else:
            flash("Error deleting task.", "error")
        return redirect(url_for("index"))

    @app.route("/export")
    def export_tasks() -> Response:
        import json

        model = TaskModel(app.config["DATABASE"])
        tasks = model.get_all()

        json_data = json.dumps(tasks, indent=2)
        return Response(
            json_data,
            mimetype="application/json",
            headers={"Content-Disposition": "attachment;filename=tasks.json"},
        )

    @app.route("/import", methods=("GET", "POST"))
    def import_tasks_view() -> Union[str, Response]:
        if request.method == "POST":
            if "file" not in request.files:
                flash("No file part", "error")
                return redirect(request.url)

            file = request.files["file"]
            if file.filename == "":
                flash("No selected file", "error")
                return redirect(request.url)

            if file:
                try:
                    import json

                    tasks_data = json.load(file)
                    mode = request.form.get("mode", "merge")

                    model = TaskModel(app.config["DATABASE"])
                    success, msg = model.import_tasks(tasks_data, mode=mode)

                    if success:
                        flash(msg or "Tasks imported successfully.", "success")
                        return redirect(url_for("index"))
                    else:
                        flash(f"Import failed: {msg}", "error")
                except json.JSONDecodeError:
                    flash("Invalid JSON file.", "error")
                except Exception as e:
                    flash(f"Error processing file: {str(e)}", "error")

        return render_template("import.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
