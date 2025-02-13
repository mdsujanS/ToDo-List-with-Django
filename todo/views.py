from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from . import models 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin 


class TaskList(LoginRequiredMixin, ListView):
    model = models.Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context 
        

class TaskDetail(LoginRequiredMixin, DetailView):
    model = models.Task 
    context_object_name = 'tasks'
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = models.Task 
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

# class TaskUpdate(UpdateView):
#     models = models.Task 
#     fields = '__all__'
#     context_object_name = 'Tasks'
#     success_url = reverse_lazy('task-list')
#     template_name = 'todo/task_update.html'

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('task-list')

class taskDelete(LoginRequiredMixin, DeleteView):
    model = models.Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('task-list')
    template_name = 'todo/task_delete.html'

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = False 
    
    def get_success_url(self):
        return reverse_lazy('task-list')

class CustomLogoutView(LogoutView):
    
    def get_success_url(self):
        return reverse_lazy('login')
    