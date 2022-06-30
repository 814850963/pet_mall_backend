from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework.mixins import *
from rest_framework import status 
from mallapi.models import Student
from .serializers import StudentModelSerializer

# Create your views here.
class StudentAPIView(APIView):
    def get(self, request):
        """获取所有学生信息"""
        # 1 从数据库中读取学生信息
        student_list = Student.objects.all()
        # 2 实例化序列化器 获取序列化对象
        serializer = StudentModelSerializer(instance=student_list, many=True)
        # 3 转换数据并返回给客户端
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentMixinView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request):
        """获取所有数据"""
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)
        """
        return self.list(request)
    
    def post(self, request):
        """添加一条数据"""
        return self.create(request)

class StudentInfoMixinView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)
