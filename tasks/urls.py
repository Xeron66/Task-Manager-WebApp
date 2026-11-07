from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    # The <int:task_id> part is a variable that catches the ID number
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
]