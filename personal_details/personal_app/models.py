from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    resume_title = models.CharField(max_length=100)
    resume_description = models.TextField()
    resume_file = models.FileField(upload_to='resumes/')
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    project_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username
