from django.db import models
from django.contrib.auth.models import User

class adminlogin(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

class register(models.Model):
    username=models.CharField(max_length=40)
     # dob = models.DateField(null=True, blank=True)
    email=models.EmailField(max_length=20)
    # gender=models.CharField(max_length=10)
    # mob=models.IntegerField()
    # qualification=models.CharField(max_length=20)
    # address = models.CharField(max_length=60)
    select = models.CharField(max_length=10)
    password = models.CharField(max_length=8)

    def __str__(self):
        return str(self.id)


class Job_Postings(models.Model):
    companyname = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    vacancyname = models.CharField(max_length=90)
    vacancytype = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    qualification = models.CharField(max_length=15)
    aboutjob = models.TextField(max_length=220)
    postedby = models.CharField(max_length=30)
    vacancy =  models.CharField(max_length=40)

    def __str__(self):
        return str(self.id)

class Applied_Jobs(models.Model):
    appliedby = models.CharField(max_length=30)
    appliedfor = models.IntegerField()
    appliedon = models.DateTimeField()
    status = models.CharField(max_length=30)

