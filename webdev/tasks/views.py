from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tasks.forms import NewTaskForm, TaskFormEdit
from webdev.tasks.models import Task

# Create your views here.
""" def home(request):
    return HttpResponse('Home de tarefas!!!') """

def home(request):
    # tasks_pending = Task.objects.filter(is_conclude = False).all()
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:home'))
        else:
            tasks_pending = Task.objects.filter(is_conclude = False).all()
            tasks_is_conclude = Task.objects.filter(is_conclude = True).all()
            return render(
                request, 
                'home.html', 
                {
                    'form': form, 
                    'tasks_pending': tasks_pending,
                    'tasks_is_conclude': tasks_is_conclude,
                }, 
                status = 400
            )
    tasks_pending = Task.objects.filter(is_conclude = False).all()
    tasks_is_conclude = Task.objects.filter(is_conclude = True).all()
    return render(
        request, 
        'home.html', 
        {
            'tasks_pending': tasks_pending,
            'tasks_is_conclude': tasks_is_conclude,
        }
    )

def details(request, task_id):
    task = Task.objects.get(id = task_id)
    form = TaskFormEdit(request.POST, instance = task)
    
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(reverse('tasks:home'))
