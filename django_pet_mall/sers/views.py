import json
from django.views import View
from django.http.response import JsonResponse
from .serializers import StudentSerializer, StudentSerializer1
from mallapi.models import Student

# Create your views here.
class StudentView(View):
    def get(self, request):
        """序列化器，序列化阶段的调用"""
        # 获取数据集
        student_list = Student.objects.all()
        # 1.实例化序列化器，得到序列化对象
        serializer = StudentSerializer(instance = student_list, many=True)
        # 2.调用序列化对象的data属性方法获取转换后的数据
        data = serializer.data
        # 3。相应数据
        return JsonResponse(data=data, status=200, safe=False, json_dumps_params={"ensure_ascii": False})

    def get1(self, request):
        """反序列化器，采用字段选项来验证数据"""
        # 1.接受客户端提交的数据
        data = json.dumps(request.body)
        data = {
            "name": "xiaohong",
            "age": -30,
            "sex": True,
            "class_num": "301",
            "description": "lalala"
        }
        # 1.1实例化序列化器，获取序列化对象
        serializer = StudentSerializer1(data=data)
        # 1.2调用序列化器进行数据验证
        ret = serializer.is_valid()
        # 1.3获取验证后的结果
        if ret:
            print(ret)
        else:
            print(ret)
        # 2.操作数据库
        data = serializer.data
        # 3。返回结果
        return JsonResponse(data=data, status=200, safe=False, json_dumps_params={"ensure_ascii": False})