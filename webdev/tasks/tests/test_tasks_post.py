from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tasks.models import Task
import pytest

@pytest.fixture
def response(client, db):
    result = client.post(
        reverse('tasks:home'), 
        data = {
            'name': 'Task'
        }
    )
    return result

def test_contains_task_database(response):
    assert Task.objects.exists()

def test_redirect_after_task_saved(response):
    assert response.status_code == 302

@pytest.fixture
def response_invalid_data(client, db):
    result = client.post(
        reverse('tasks:home'),
        data = {
            'name': ''
        }
    )
    return result

def test_not_contains_task_database(response_invalid_data):
    assert not Task.objects.exists()

def test_page_with_invalid_datas(response_invalid_data):
    assert response_invalid_data.status_code == 400
