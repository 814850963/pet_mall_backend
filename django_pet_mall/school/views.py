from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import TeacherModelSerializer, StudentModelSerializer

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

# Create your views here.
