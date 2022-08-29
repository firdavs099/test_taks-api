from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_desc = models.TextField()
    was_published = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    