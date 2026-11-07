from django.db import models

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')

    # ToDo: We will store Tailwind CSS color classes here (e.g., 'bg-red-100')
    color = models.CharField(max_length=50, default='bg-white')

    # ToDo: For future drag-and-drop sorting
    order = models.IntegerField(default=0)
    
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title