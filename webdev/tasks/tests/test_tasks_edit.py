from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

from webdev.tasks.models import Task

# Tarefa pendente
@pytest.fixture
def task_pending(db):
    return Task.objects.create(name = 'Tarefa 1', is_conclude = False)

@pytest.fixture
def response_with_task_pending(client, task_pending):
    result = client.post(
        reverse(
            'tasks:details', 
            kwargs = {
                'task_id': task_pending.id
            }
        ),
        data = {
            'is_conclude': 'true',
            'name': f'{task_pending.name} - editada'
        }
    )
    return result

def test_status_code(response_with_task_pending):
    assert response_with_task_pending.status_code == 302

def test_task_is_conclude(response_with_task_pending):
    assert Task.objects.first().is_conclude

# Tarefa Concluída
@pytest.fixture
def task_is_conclude(db):
    return Task.objects.create(name = 'Tarefa 1', is_conclude = True)

@pytest.fixture
def response_with_task_is_conclude(client, task_is_conclude):
    result = client.post(
        reverse(
            'tasks:details', 
            kwargs = {
                'task_id': task_is_conclude.id
            }
        ),
        data = {
            'name': f'{task_is_conclude.name} - editada'
        }
    )
    return result

def test_task_pending(response_with_task_is_conclude):
    assert not Task.objects.first().is_conclude
