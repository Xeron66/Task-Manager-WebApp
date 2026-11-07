from django.shortcuts import render
from .models import Task

def task_list(request):
    # Grab all the taks from the DB
    tasks = Task.objects.filter(is_completed=False)
    # Hand them off to an HTML file to display them
    return render(request, "tasks/list.html", {"tasks": tasks})
