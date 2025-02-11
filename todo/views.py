from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models 

class TaskList(ListView):
    model = models.Task
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = models.Task 
    context_object_name = 'tasks'
    
    