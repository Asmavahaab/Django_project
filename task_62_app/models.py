# Create your models here.
# class user_home(models.Model):
#     username = models.CharField('username')
#     first_name = models.CharField('first_name')
#     last_name = models.CharField('last_name')
#     email = models.EmailField('email')
#     password = models.CharField('password')
#     cpassword = models.CharField('password1')
#
#     def __str__(self):
#         return '{}'.format(self.username)
import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to ='images/',blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    mother_tongue = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)

class contact_details(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    linkedin_handle = models.URLField(blank=True)
    insta_handle = models.URLField(blank=True)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title



class project_showcase(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200,blank=True)
    technologies_used = models.CharField(max_length=1000,blank=True)
    project_images = models.ImageField(upload_to='images/',blank=True)
    project_description = models.TextField(max_length=2000,blank=True)
    project_link = models.URLField(blank=True)

class work_experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,blank=True)
    job_title = models.CharField(max_length=200,blank=True)
    mode = models.CharField(max_length=6)
    start_date = models.DateField(blank=True)
    duration = models.CharField(max_length=10)
    responsibilities = models.TextField(max_length=10000)


class education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=200)
    institute = models.CharField(max_length=500, blank=True)
    board = models.CharField(max_length=100, blank=True)
    aggregrate_marks = models.IntegerField(blank=True)
    year_of_passing = models.IntegerField(validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year+10)
        ],blank=True)

class certifications(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    issuing_organisation = models.CharField(max_length=200)
    date_of_issue = models.DateField(blank=True)
    certificate_link = models.URLField(blank=True)
