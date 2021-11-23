from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    description = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=32)
    school = models.CharField(max_length=64)
    projects = models.ManyToManyField('Project', related_name='students')
    git_profile = models.CharField(max_length=256)
    skills = models.ManyToManyField()


class Resume(models.Model):
    name = models.CharField("name", max_length=25)
    description = models.CharField("description", max_length=300)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    name = models.CharField("name", max_length=50)
    description = models.CharField("description",max_length=500)
    git_url = models.CharField("git_url", max_length=50)
    video_url = models.TextField("video_url")
    realisation_time = models.DateField("realisation_time")






class Image(models.Model):
    image = models.ImageField("image")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)