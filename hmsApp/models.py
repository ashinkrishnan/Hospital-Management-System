

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#   PATIENT MODEL
class Patient(models.Model):
    username = models.CharField(max_length=200,null=True)
    email= models.EmailField(unique=True)
    contactnumber = models.CharField(max_length=11,null=True)

    def __str__(self):
        return self.username


# CARDIO MODEL        
class CardioDoc(models.Model):
    name = models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phoneNumber=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    specializations= models.CharField(max_length=50)

    def __str__(self):
        return self.name
#ORTHO MODEL
class OrthoDoc(models.Model):
    name = models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phoneNumber=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    specializations= models.CharField(max_length=50)

    def __str__(self):
        return self.name

#UROLOGY MODEL
class UroDoc(models.Model):
    name = models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phoneNumber=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    specializations= models.CharField(max_length=50)

    def __str__(self):
        return self.name

#PULMONOLOGY MODEL
class PulmonoDoc(models.Model):
    name = models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phoneNumber=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    specializations= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctorname = models.CharField(max_length=50)
    doctormail = models.EmailField(max_length=50)
    patientname= models.CharField(max_length=50)
    patientmail= models.EmailField(max_length=50)
    appointmentdate=models.DateField()
    appointmenttime=models.TimeField()
    symptoms=models.CharField(max_length=200)
    prescription =models.CharField(max_length=200)
    status = models.BooleanField()

    def __str__(self):
        return self.patientname +"booked an appointment with doctor:"+self.doctorname+" on "+str(self.appointmentdate)



