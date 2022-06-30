from decimal import Clamped
from tabnanny import verbose
from django.db import models

# Create your models here.
class Student(models.Model):
    # 模型字段
    name = models.CharField(max_length=100, verbose_name="xingming")
    sex = models.BooleanField(default=1, verbose_name="sex")
    age = models.IntegerField(verbose_name="age", null=True)
    class_num = models.CharField(max_length=5, verbose_name="class num")
    description = models.TextField(max_length=1000, verbose_name="person description")

    class Meta:
        db_table = "tb_student"
        verbose_name = "student"
        verbose_name_plural = verbose_name
