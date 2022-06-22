from rest_framework import serializers
from mallapi.models import Student
"""
serializers 是drf提供给开发者调用的序列化器模块
Serializer 序列化器积累 
ModelSerializer 最常用的类
"""
class StudentSerializer(serializers.Serializer):
    """学生信息序列化器"""
    # 1 字段转换的声明
    # 字段 = serializers.字段类型
    id = serializers.IntegerField()
    name = serializers.CharField()
    sex = serializers.BooleanField()
    age = serializers.IntegerField()
    description = serializers.CharField()

    # 2如果集成的事ModelSerializer，需要生命调用的模型信息
    # class Meta:
    #     model=模型
    #     fields = ["字段1","字段2"]

    # # 3验证代码的对象方法
    # def validate(self, attrs): # 是固定的
    #     ...
    #     return attrs
    
    # def validate_<字段名>(self, data): # 是固定的
    #     ...
    #     return attrs
    
    # # 4模型操作的方法
    # def create(self, validated_data): # 完成添加操作
    #     ...
    # def update(self, instance, validated_data): # 更新数据操作
    #     ...

def check_classmate(data):
    if len(data) != 3:
        raise serializers.ValidationError(detail="班级编号格式不正确！",code="check classmate")
    return data

class StudentSerializer1(serializers.Serializer):
    """学生信息序列化器"""
    # 1 字段转换的声明
    # 字段 = serializers.字段类型
    id = serializers.IntegerField(read_only=True) # 在客户端提交数据的反序列化阶段不会执行
    name = serializers.CharField(required=True) # 反序列化阶段必填
    sex = serializers.BooleanField(default=True) # 反序列化阶段，客户端没有提交则默认为True
    age = serializers.IntegerField(max_value=100, min_value=0, error_messages={
        "min_value":"the age filed must be 0<= <=100",
        "max_value":"the age is too big"}) # age在反序列化阶段必须是0<=age<=100
    classmate = serializers.CharField(validators=[check_classmate])
    description = serializers.CharField(allow_null=True, allow_blank=True) # 允许为空或者为None

    # 2如果集成的事ModelSerializer，需要生命调用的模型信息
    # class Meta:
    #     model=模型
    #     fields = ["字段1","字段2"]

    # # 3验证代码的对象方法
    # def validate(self, attrs): # 是固定的
    #     ...
    #     return attrs
    
    # def validate_<字段名>(self, data): # 是固定的
    #     ...
    #     return attrs

    def validate(self, attrs):
        """
        验证来自客户端的所有数据
        validate是固定方法名
        参数attrs是在序列化器实例化时的data数据
        """
        print(f"attrs={attrs}")
        if attrs["classmate"] == "307" and attrs["sex"]:
            raise serializers.ValidationError(detail="classmate错误", code="validate_classmate")
        return attrs
    
    def validate_name(self, data):
        """
        验证单个字段
        方法名的格式必须以 validate_<字段名>为名称，否则序列化器不识别
        validate开头方法会自动被is_valid调用
        """
        print(f"name={data}")
        if data in ["python", "django"]:
            raise serializers.ValidationError(detail="学生姓名不能是python或者django", code="validate_name")
        return data

    # # 4模型操作的方法
    # def create(self, validated_data): # 完成添加操作
    #     ...
    # def update(self, instance, validated_data): # 更新数据操作
    #     ...