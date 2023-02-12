from django.db import models
from django_cryptography.fields import encrypt

class Patient(models.Model):

    first_name = encrypt(models.CharField(max_length=100))
    last_name = encrypt(models.CharField(max_length=100))
    address = encrypt(models.CharField(max_length=500))
    # With this method of encryption, this error is raised by the shell when trying to encrypt
    # the EmailField:

    # django.core.exceptions.FieldError: Unsupported lookup 'exact' for EncryptedEmailField 
    # or join on the field not permitted, perhaps you meant exact or iexact?
    
    # Apparently, people had similar issues in the past but with the CharField
    # and I saw it was intended, see the Github issue below
    # https://github.com/georgemarshall/django-cryptography/issues/84
    # However, now the CharField is encryptable
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