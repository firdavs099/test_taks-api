from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
