import io


def test_export_tasks(client, app):
    client.post("/tasks/add", data={"title": "Export Me"}, follow_redirects=True)

    response = client.get("/export")
    assert response.status_code == 200
    assert response.headers["Content-Disposition"].startswith("attachment;")
    assert b"Export Me" in response.data


def test_import_tasks_replace(client, app):
    client.post("/tasks/add", data={"title": "Will Be Replaced"}, follow_redirects=True)

    json_data = b'[{"id": "1", "title": "Imported Replace", "status": "pending", "created_at": "2026-05-17T10:00:00Z"}]'
    data = {"file": (io.BytesIO(json_data), "tasks.json"), "mode": "replace"}

    response = client.post(
        "/import", data=data, content_type="multipart/form-data", follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Will Be Replaced" not in response.data
    assert b"Imported Replace" in response.data


def test_import_tasks_merge(client, app):
    client.post("/tasks/add", data={"title": "Keep Me"}, follow_redirects=True)

    json_data = b'[{"id": "2", "title": "Imported Merge", "status": "pending", "created_at": "2026-05-17T10:00:00Z"}]'
    data = {"file": (io.BytesIO(json_data), "tasks.json"), "mode": "merge"}

    response = client.post(
        "/import", data=data, content_type="multipart/form-data", follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Keep Me" in response.data
    assert b"Imported Merge" in response.data


def test_import_invalid_file(client, app):
    data = {"file": (io.BytesIO(b"{invalid}"), "tasks.json"), "mode": "merge"}
    response = client.post(
        "/import", data=data, content_type="multipart/form-data", follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Invalid JSON file" in response.data
