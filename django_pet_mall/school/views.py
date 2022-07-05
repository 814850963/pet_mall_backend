from rest_framework.viewsets import ModelViewSet
from .serializers import TeacherModelSerializer, StudentModelSerializer
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from .models import Student

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [SessionAuthentication, BaseAuthentication]
    permission_classes = [IsAdminUser, IsAuthenticated]

# Create your views here.
