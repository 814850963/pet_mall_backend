from rest_framework import serializers
from school.models import Teacher, Student, Achievement,Course

class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class CourseModelSerializer(serializers.ModelSerializer):
    teacher = TeacherModelSerializer()
    class Meta:
        model = Course
        fields = ["name","teacher"]

class AchievementModelSerializer(serializers.ModelSerializer):
    # course = CourseModelSerializer()
    # course_name = serializers.CharField(source="course.name")
    # student_name = serializers.CharField(source="student.age")
    class Meta:
        model = Achievement
        fields = "__all__"
        depth = 2

class StudentModelSerializer(serializers.ModelSerializer):
    s_achievement = AchievementModelSerializer(many=True)
    class Meta:
        model = Student
        fields = "__all__"