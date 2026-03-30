from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(verbose_name='Bio', max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True,)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}_{self.username}'


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}_{self.title}'