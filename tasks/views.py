from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    # 1. Did the user just submit the form?
    if request.method == "POST":
        # Grab the text they typed into the input field named 'title'
        task_title = request.POST.get("title")
        
        # Create a new row in the SQL database
        Task.objects.create(title=task_title)
        
        # Refresh the page so they don't submit the same form twice by accident
        return redirect("task_list")
        
    # 2. If they just loaded the page normally, grab the pending tasks
    tasks = Task.objects.filter(is_completed=False)
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def complete_task(request, task_id):
    # Find the specific task in the database using its unique ID
    task = Task.objects.get(id=task_id)
    
    # Change its status to True
    task.is_completed = True
    
    # Save the change to the database
    task.save()
    
    # Send the user back to the main list
    return redirect("task_list")