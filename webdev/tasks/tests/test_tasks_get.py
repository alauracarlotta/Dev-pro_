from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest


@pytest.fixture
def response(client):
    result = client.get(reverse('tasks:home'))
    return result

# Create your tests here.
def test_status_code(response):
    assert response.status_code == 200

def test_form_contains(response):
    assertContains(response, '<form')

def test_save_button_contains(response):
    assertContains(response, '<button type="submit"')
