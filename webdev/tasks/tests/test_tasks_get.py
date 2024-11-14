from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

from webdev.tasks.models import Task


@pytest.fixture
def response(client, db):
    result = client.get(reverse('tasks:home'))
    return result

def test_status_code(response):
    assert response.status_code == 200

def test_form_contains(response):
    assertContains(response, '<form')

def test_save_button_contains(response):
    assertContains(response, '<button type="submit"')

@pytest.fixture
def tasks_list_pending(db):
    tasks = [
        Task(name = 'Tarefa 1', is_conclude = False)
    ]
    Task.objects.bulk_create(tasks)
    return tasks

@pytest.fixture
def response_with_tasks_list_pending(client, tasks_list_pending):
    result = client.get(reverse('tasks:home'))
    return result

def test_tasks_list_pending_contains(response_with_tasks_list_pending, tasks_list_pending):
    for task in tasks_list_pending:
        assertContains(response_with_tasks_list_pending, task.name)
