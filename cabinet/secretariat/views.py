from rest_framework.viewsets import ModelViewSet

from secretariat.serializers import PatientSerializer
from secretariat.models import Patient

class PatientViewset(ModelViewSet):

    serializer_class = PatientSerializer

    def get_queryset(self):
        return Patient.objects.all()
