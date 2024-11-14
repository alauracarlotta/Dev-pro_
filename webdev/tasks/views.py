from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tasks.forms import NewTaskForm
from webdev.tasks.models import Task

# Create your views here.
""" def home(request):
    return HttpResponse('Home de tarefas!!!') """

def home(request):
    # pending_tasks = Task.objects.filter(is_conclude = False).all()
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:home'))
        else:
            pending_tasks = Task.objects.filter(is_conclude = False).all()
            return render(request, 'home.html', {'form': form, 'pending_tasks': pending_tasks}, status = 400)
    pending_tasks = Task.objects.filter(is_conclude = False).all()
    return render(request, 'home.html', {'pending_tasks': pending_tasks})
