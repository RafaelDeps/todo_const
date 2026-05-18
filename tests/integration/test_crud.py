def test_dashboard_empty(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"TODO List" in response.data


def test_add_task(client):
    response = client.post(
        "/tasks/add",
        data={"title": "Test Integration", "description": "Test Desc"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Test Integration" in response.data
    assert b"Task added successfully" in response.data


def test_toggle_task(client, app):
    # Add first
    client.post("/tasks/add", data={"title": "Toggle Me"})
    # Find ID from model directly for simplicity in testing
    from src.models.task import TaskModel

    model = TaskModel(app.config["DATABASE"])
    task = model.get_all()[0]

    response = client.post(f"/tasks/{task['id']}/toggle", follow_redirects=True)
    assert response.status_code == 200

    updated_task = TaskModel(app.config["DATABASE"]).get_all()[0]
    assert updated_task["status"] == "done"


def test_update_task(client, app):
    client.post("/tasks/add", data={"title": "Old Title"})
    from src.models.task import TaskModel

    model = TaskModel(app.config["DATABASE"])
    task = model.get_all()[0]

    response = client.post(
        f"/tasks/{task['id']}/update",
        data={"title": "New Title"},
        follow_redirects=True,
    )
    assert response.status_code == 200

    updated_task = TaskModel(app.config["DATABASE"]).get_all()[0]
    assert updated_task["title"] == "New Title"


def test_delete_task(client, app):
    client.post("/tasks/add", data={"title": "Delete Me"})
    from src.models.task import TaskModel

    model = TaskModel(app.config["DATABASE"])
    task = model.get_all()[0]

    response = client.post(f"/tasks/{task['id']}/delete", follow_redirects=True)
    assert response.status_code == 200
    assert b"Delete Me" not in response.data

    assert len(TaskModel(app.config["DATABASE"]).get_all()) == 0
