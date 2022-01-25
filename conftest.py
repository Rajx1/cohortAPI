import pytest
import app
from controllers import students

@pytest.fixture
def api(monkeypatch):
    test_students = [
        {'id': 1, 'name': 'Test Student 1'},
        {'id': 2, 'name': 'Test Student 2'}
    ]
    monkeypatch.setattr(students, "students", test_students)
    api = app.app.test_client()
    return api