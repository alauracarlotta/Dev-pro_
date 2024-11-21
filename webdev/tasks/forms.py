from django.forms import ModelForm

from webdev.tasks.models import Task


class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name']

class TaskFormEdit(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'is_conclude']
