from django.urls import path
from .import views 


urlpatterns=[
    path('', views.TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-details'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.taskDelete.as_view(),name='task-delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.Registerpage.as_view(), name='register'),
    
    
    
    
    
]
