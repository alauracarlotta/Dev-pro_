from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

from webdev.tasks.models import Task

# Tarefa pendente
@pytest.fixture
def delete_task(db):
    return Task.objects.create(name = 'Tarefa 1', is_conclude = True)

@pytest.fixture
def response_delete_task(client, delete_task):
    result = client.post(reverse(
        'tasks:delete', 
        kwargs = {
            'task_id': delete_task.id
        }
    ))
    return result

def test_delete_task(response_delete_task):
    assert not Task.objects.exists()
