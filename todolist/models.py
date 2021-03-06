from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    perfomed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}{self.perfomed}'
