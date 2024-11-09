from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    languages = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    hobbies = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


class Qualification(models.Model):
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    year = models.IntegerField()
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=100)
    certificate_image = models.ImageField(upload_to='certificates/')
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
