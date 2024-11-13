from django.urls import path
from webdev.tasks import views


app_name = 'tasks'

urlpatterns = [
    path('', views.home, name = 'home'),
]
