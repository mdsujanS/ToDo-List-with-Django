from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from . import models 

class TaskList(ListView):
    model = models.Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = models.Task 
    context_object_name = 'tasks'
    
class TaskCreate(CreateView):
    model = models.Task 
    fields = "__all__"
    success_url = reverse_lazy('task-list')

# class TaskUpdate(UpdateView):
#     models = models.Task 
#     fields = '__all__'
#     context_object_name = 'Tasks'
#     success_url = reverse_lazy('task-list')
#     template_name = 'todo/task_update.html'

class TaskUpdate(UpdateView):
    model = models.Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')

class taskDelete(DeleteView):
    model = models.Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_delete.html'