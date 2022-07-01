from email.mime import base
from django.contrib import admin
from django.urls import path, include, re_path
from. import views

urlpatterns = [
   
   
]

# 自动生成路由信息
from rest_framework.routers import SimpleRouter, DefaultRouter

# 实例化路由类
router = DefaultRouter()

# 给路由注册视图集
router.register("student", views.StudentModelViewSet, basename="student")

# 把生成的路由列表和urlpatterns进行拼接组合
urlpatterns += router.urls