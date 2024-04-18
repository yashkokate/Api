from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by=models.CharField(max_length=20)


class Project(models.Model):
    Project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    created_by=models.CharField(max_length=20)
    user = models.ManyToManyField(User) 



