from rest_framework.serializers import ModelSerializer, ValidationError

from secretariat.models import Patient, Consultation

class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'address', 'email']

    # To ensure the unicity of the mailing address when creating a new Patient entry
    def validate_email(self, value):
        if Patient.objects.filter(email=value).exists():
            raise ValidationError('This mailing address is already used. Choose an other one.')
        return value

class ConsultationSerializer(ModelSerializer):

    class Meta:
        model = Consultation
        fields = ['id', 'date', 'patient', 'nom', 'description', 'type']