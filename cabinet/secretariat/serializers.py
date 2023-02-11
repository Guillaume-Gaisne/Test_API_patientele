from rest_framework.serializers import ModelSerializer, ValidationError

from secretariat.models import Patient, Consultation

class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'adress', 'email']

    def validate_email(self, value):
        if Patient.objects.filter(email=value).exists():
            raise ValidationError('Cet email existe déjà')
        return value

class ConsultationSerializer(ModelSerializer):

    class Meta:
        model = Consultation
        fields = ['id', 'date', 'patient', 'nom', 'description', 'type']