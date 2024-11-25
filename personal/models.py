from django.db import models
from django.utils.timezone import now

class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title

class GuestBook(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
