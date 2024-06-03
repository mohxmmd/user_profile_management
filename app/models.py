from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):

    bio = models.CharField(max_length=100,blank=True)
    skills = models.CharField(max_length=100, blank=True)
    contact_details = models.CharField(max_length=100, blank=True)

class Portfolio(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null= True)
    projects = models.TextField(blank=True)
    work_experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE , null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True)
    link = models.URLField()