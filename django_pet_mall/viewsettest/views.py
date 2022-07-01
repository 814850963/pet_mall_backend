from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet

from rest_framework.response import Response
from rest_framework.mixins import *
from rest_framework import status 
from mallapi.models import Student
from .serializers import StudentModelSerializer
from rest_framework.decorators import action

# Create your views here.
class StudentAPIView(APIView):
    @action(methods=["get"], detail=False, url_path="/user/login")
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

class StudentViewSet(ViewSet):
    def get_list(self, request):
        student_list = Student.objects.all()
        serializer = StudentModelSerializer(instance=student_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =  StudentModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_student_info(self, request, pk):
        print(request)
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentModelSerializer(instance=student)

        return Response(serializer.data)

    def update(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentModelSerializer(instance=student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    def delete(self,request, pk):
        try:
            Student.objects.get(pk=pk).delete()
        except Student.DoesNotExist:
            ...
        return Response(status=status.HTTP_204_NO_CONTENT)