from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from secretariat.serializers import PatientSerializer, ConsultationSerializer
from secretariat.models import Patient, Consultation
from secretariat.permissions import IsAdminAuthenticated

class PatientViewset(ModelViewSet):

    serializer_class = PatientSerializer

    # IsAdminAuthenticated allows anyone to access the list of patients
    # with a GET request but forbids non superuser to POST, PUT/PATCH or DELETE
    permission_classes = [IsAdminAuthenticated]
    queryset = Patient.objects.all()


class ConsultationViewset(ModelViewSet):

    serializer_class = ConsultationSerializer

    def get_queryset(self):
        queryset = Consultation.objects.all()

        # To allow the access to the consultations of a particuler patient
        # with the parameter 'patient_id= int' in the URL request
        patient_id = self.request.GET.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient_id=patient_id)
        
        return queryset
