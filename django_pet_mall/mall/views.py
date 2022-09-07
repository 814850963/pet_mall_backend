from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from mallapi.models import Student
from .serializers import StudentModelSerializer, BulkCreateSerializer
# Create your views here.

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = BulkCreateSerializer

def index(request):
    return render(request)