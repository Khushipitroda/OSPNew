from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django import forms

policy_type = (
    ('Subsidy', 'Subsidy'),
    ('Scheme', 'Scheme'),
)

govt_type = (
    ('School', 'School'),
    ('College', 'College'),
    ('Hospital', 'Hospital'),
    ('Police Station', 'Police Station'),
    ('Court', 'Court'),
    ('Office', 'Office'),
)

cast_type = (
    ('General', 'General'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    ('OBC', 'OBC'),
    ('Other', 'Other'),
)

role_type = (
    ('Citizen', 'Citizen'),
    ('Government_Employee', 'Government_Employee'),
)
occupation_type = (
    ('Farmer', 'Farmer'),
    ('House wife', 'House wife'),
    ('Self-Employed', 'Self-Employed'),
    ('Doctor', 'Doctor'),
    ('Government-Job', 'Government-Job'),
    ('Student', 'Student'),
    ('Other', 'Other'),
)

class Policiess(models.Model):
    name = models.CharField(max_length=100)
    policies_for = models.CharField(choices=occupation_type, max_length=50)
    logo = models.ImageField(upload_to='pics')
    type = models.CharField(choices=policy_type, default='Subsidy', max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)
    desc = models.CharField(max_length=1000)


class Govt_Bodiess(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pics')
    type = models.CharField(choices=govt_type, default='School', max_length=50)
    address = models.CharField(max_length=1000)
    contact = models.CharField(max_length=15)
    desc = models.CharField(max_length=500)


class Post_Bills(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pics')
    date = models.DateTimeField(default=datetime.now, blank=True)
    desc = models.CharField(max_length=1000)


class Post_Announcements(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pics')
    date = models.DateTimeField(default=datetime.now, blank=True)
    doc = models.FileField(upload_to='files',blank=True)


class Post_Newss(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='pics')
    date = models.DateTimeField(default=datetime.now, blank=True)
    desc = models.CharField(max_length=1000)


gender_type = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class Adhar_Card(models.Model):
    anumber = models.CharField(max_length=12)
    fname = models.CharField(max_length=20)
    mname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=(('M', 'MALE'), ('F', 'FEMALE')), default='')
    address = models.CharField(max_length=1000)
    contact = models.CharField(max_length=10)
    dob = models.DateField(default=datetime.now)
    cast = models.CharField(choices=cast_type, default='General', max_length=50)
    scan = models.FileField(upload_to='files', blank=True)


class Registration(models.Model):
    r_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anumber = models.CharField(max_length=20)
    role = models.CharField(choices=role_type, max_length=50)
    contact = models.CharField(max_length=20)
    occupation = models.CharField(choices=occupation_type, max_length=50)

    def __str__(self):
        return self.user.first_name


class Feedback(models.Model):
    anumber = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    cno = models.CharField(max_length=15)
    message = models.CharField(max_length=1000)


class Upload_doc(models.Model):
    anumber = models.ForeignKey(User, on_delete=models.CASCADE)
    Adhar_card = models.FileField(upload_to='files',default="None")
    Pan_card = models.FileField(upload_to='files',default="None")
    Voterid_card = models.FileField(upload_to='files',default="None")
    Rashan_card = models.FileField(upload_to='files',default="None")
    Passport = models.FileField(upload_to='files',default="None")
    R_C_Book = models.FileField(upload_to='files',default="None")
    Driving_licence = models.FileField(upload_to='files',default="None")
    Income_certi = models.FileField(upload_to='files',default="None")
    Noncriminal_certi = models.FileField(upload_to='files',default="None")
    Other = models.FileField(upload_to='files', default="None")
