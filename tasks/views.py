
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from .models import Task
from datetime import date


def task_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date_str = request.POST.get("due_date") or None
        priority = request.POST.get("priority")
        color = request.POST.get("color")

        # Convert the submitted date
        due_date = None

        if due_date_str:
            try:
                due_date = date.fromisoformat(due_date_str)
            except ValueError:
                return JsonResponse({
                    "success": False,
                    "error": "Please enter a valid due date."
                }, status=400)

            # Validate the due date
            if due_date < timezone.localdate():
                return JsonResponse({
                    "success": False,
                    "error": "You cannot create a task with a due date in the past!"
                }, status=400)

        # Create task if validation passes
        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            color=color
        )

        return JsonResponse({
            "success": True,
            "message": "Task created successfully!"
        })

    tasks = Task.objects.filter(is_completed=False)

    return render(request, "tasks/task_list.html", {
        "tasks": tasks
    })


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = True
    task.save()

    return redirect("task_list")
