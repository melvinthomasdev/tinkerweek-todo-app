from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)
    # date_added = models.DateTimeField(auto_now_add=True)

    # category = models.CharField(max_length=35, choices=(
    #     ('option1', 'option1'),
    #     ('option2', 'optiqon2'),
    #     ('option3', 'option3'),
    #     ('option4', 'option4'),
    # ))

    def __str__(self):
        return self.title