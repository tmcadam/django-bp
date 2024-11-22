from django.db import models

class Device(models.Model):

    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
