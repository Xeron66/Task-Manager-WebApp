from django.urls import path
from . import views

urlpatterns = [
    # The empty string '' means this is the default page for this app
    path('', views.task_list, name='task_list'),
]