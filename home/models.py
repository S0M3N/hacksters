import email
from email import message
from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    course = models.CharField(max_length=10)
    branch = models.CharField(max_length=70, null=True, blank=True)
    year = models.CharField(max_length=4, null= True, blank= True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

    def __str__(self):
        val = self.fname + " " + self.course
        return val

class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        val = self.fname+ " " + self.subject
        return val