from rest_framework.serializers import ModelSerializer

from secretariat.models import Patient

class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'adress', 'email']