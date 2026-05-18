import pytest
from flask import Flask
from src.app import create_app
import tempfile
import os


@pytest.fixture
def app():
    # Use a temporary directory for tests so we don't overwrite real tasks.json
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({"TESTING": True, "DATABASE": db_path})
    yield app
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app: Flask):
    return app.test_client()


@pytest.fixture
def runner(app: Flask):
    return app.test_cli_runner()
