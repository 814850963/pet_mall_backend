from rest_framework.viewsets import ModelViewSet
from mallapi.models import Student
from .serializers import StudentModelSerializer, BulkCreateSerializer
# Create your views here.

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = BulkCreateSerializer

