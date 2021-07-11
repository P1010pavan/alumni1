from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(default="")
    message = models.TextField(null=True)

    def __str__(self):
        return self.name

class Upload(models.Model):
    Name = models.CharField(max_length=50)
    Title = models.CharField(max_length=200)
    Date = models.DateField(auto_now=True)
    Description=models.TextField(null=True)
    Image = models.ImageField(upload_to='story/',default="")
    email = models.EmailField(default="")

    def __str__(self):
        return self.Name

class Job_upload(models.Model):
    Role = models.CharField(max_length=50)
    Title = models.CharField(max_length=200)
    Date = models.DateField(auto_now=True)
    Description = models.TextField(null=True)

    def __str__(self):
        return self.Role