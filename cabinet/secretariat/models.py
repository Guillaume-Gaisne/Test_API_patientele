from django.db import models

class Patient(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.CharField(max_length=500)
    email = models.EmailField()