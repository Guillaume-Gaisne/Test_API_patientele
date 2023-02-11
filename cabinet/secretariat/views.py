from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from secretariat.serializers import PatientSerializer
from secretariat.models import Patient
from secretariat.permissions import IsAdminAuthenticated

class PatientViewset(ModelViewSet):

    serializer_class = PatientSerializer

    # Only authenticated administratos 
    permission_classes = [IsAdminAuthenticated]
    queryset = Patient.objects.all()

    # def get(self, request, view):
    #     breakpoint()
    #     content = {
    #         'status': 'request was permitted'
    #     }
    #     return Response(content)

    # def get_queryset(self):
    #     return Patient.objects.all()
