from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from faker import Faker

from secretariat.models import Patient

ADMIN_LOGIN = 'admin'
PASSWORD_LOGIN = '123'

NB_ENTRIES = 5
CHOICE_NATIONALITY = 'fr_FR'

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        # Reseting the list of users and creating a superuser profil
        User.objects.all().delete()
        User.objects.create_superuser(username=ADMIN_LOGIN, password=PASSWORD_LOGIN)


        fake_patient = Faker(CHOICE_NATIONALITY)

        for _ in range(NB_ENTRIES):
            first_name, last_name = fake_patient.name().split(' ', maxsplit=1)
            email = '.'.join((first_name, last_name)) + '@mail.xyz'
            email = email.replace(' ', '_')
            address = fake_patient.address()
            Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                address=address,
            )
