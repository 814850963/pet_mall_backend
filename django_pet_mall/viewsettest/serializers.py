from rest_framework import serializers
from mallapi.models import Student

class BasicModelSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = "__all__"
                
class BulkCreateSerializer(serializers.ListSerializer):
            child = BasicModelSerializer()

class StudentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"
        # fields = ["name", "id"]
