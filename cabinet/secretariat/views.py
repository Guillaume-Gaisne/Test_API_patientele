from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from secretariat.serializers import PatientSerializer, ConsultationSerializer
from secretariat.models import Patient, Consultation
from secretariat.permissions import IsAdminAuthenticated

class PatientViewset(ModelViewSet):

    serializer_class = PatientSerializer

    # Only authenticated administratos 
    permission_classes = [IsAdminAuthenticated]
    queryset = Patient.objects.all()


    # def get_queryset(self):
    #     return Patient.objects.all()

class ConsultationViewset(ModelViewSet):

    serializer_class = ConsultationSerializer

    def get_queryset(self):
        queryset = Consultation.objects.all()

        patient_id = self.request.GET.get('patient_id')

        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
