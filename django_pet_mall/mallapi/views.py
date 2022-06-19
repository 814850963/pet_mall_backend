from os import stat
import json
from django.views import View
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.
"""
POSt /students/ 添加一个学生信息
GET /students/ 获取所有学生信息

GET /students/<pk>/ 获取一个学生信息
PUT /students/<pk>/ 更新一个学生信息
DELETE /students/<pk>/ 删除一个学生信息

一个路由对应一个视图类，所以我们可以把5个API分成两个类来完成
"""
class StudentView(View):
    """学生视图"""
    @csrf_exempt
    def post(self,request):
        """
        添加一个学生信息
        """
        # 接受客户提交的数据
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        class_num = request.POST.get("class_num")
        description = request.POST.get("description")
        # 验证数据

        # 操作数据库，保存数据
        instance = Student.objects.create(
            name=name,
            sex=sex,
            age=age,
            class_num=class_num,
            description=description,
        )
        # 返回结果
        return JsonResponse(data={
            "id": instance.pk
        }, status=201)

    def get(self,request):
        """获取多个学生信息"""
        # 1 读取数据库
        students_list = list(Student.objects.values())

        # 2 返回数据
        return JsonResponse(data=students_list, status=200, safe=False)

class StudentInfoView(View):
    def get(self, request, pk):
        """一条数据"""
        try:
            instance = Student.objects.get(pk=pk)
            return JsonResponse(data={"id": instance.pk}, status=200, safe=False)
        except Student.DoesNotExist:
            return JsonResponse(data=None, status=404)
    
    def put(self, request, pk):
        """更新一个学生数据"""
        # 接受客户提交的数据
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        class_num = request.POST.get("class_num")
        description = request.POST.get("description")
        # 验证数据

        # 操作数据库，保存数据
        try:
            instance = Student.objects.get(pk=pk)
            instance.name = name
            instance.sex = sex
            instance.age = age
            instance.class_num = class_num
            instance.description = description
            instance.save()
            return JsonResponse(data={"id": instance.pk}, status=200, safe=False)
        except Student.DoesNotExist:
            return JsonResponse(data=None, status=404)
