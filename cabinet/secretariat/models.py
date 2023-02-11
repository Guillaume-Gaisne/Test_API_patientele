from django.db import models

class Patient(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=500)
    email = models.EmailField()

class Consultation(models.Model):

    class Type(models.TextChoices):
        VISITE = 'visite'
        SUIVI = 'suivi'
        OPERATION = 'operation'

    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
    nom = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(choices=Type.choices, max_length=10)