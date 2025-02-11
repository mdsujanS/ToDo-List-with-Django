from django.urls import path
from .import views 
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-details'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.taskDelete.as_view(),name='task-delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
    
    
]
