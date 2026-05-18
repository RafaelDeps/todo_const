from datetime import datetime, timedelta, timezone


def test_add_task_with_reminder(client):
    future_time = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
    response = client.post(
        "/tasks/add",
        data={
            "title": "Task with Reminder",
            "description": "Desc",
            "reminder_at": future_time,
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Task with Reminder" in response.data
    # Convert datetime format slightly for basic string check since the HTML may display it differently
    # Let's just check if it was added. We'll do a model check to be certain.


def test_add_task_with_past_reminder(client):
    past_time = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    response = client.post(
        "/tasks/add",
        data={"title": "Past Task", "reminder_at": past_time},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"future date" in response.data.lower()
