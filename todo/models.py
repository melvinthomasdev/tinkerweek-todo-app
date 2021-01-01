from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.title