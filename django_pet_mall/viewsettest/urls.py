from email.mime import base
from django.contrib import admin
from django.urls import path, include, re_path
from. import views

urlpatterns = [
    path('students/', views.StudentAPIView.as_view()),
    path('students1/', views.StudentMixinView.as_view()),
    re_path("^students3/(?P<pk>\d+)/$}", views.StudentInfoMixinView.as_view()),

    # 视图集 ViewSet
    path("students5/", views.StudentViewSet.as_view({"get": "get_list", "post":"post"})),
    re_path("^students5/(?P<pk>\d+)/$", views.StudentViewSet.as_view({"get": "get_student_info"})),
]

# 自动生成路由信息
from rest_framework.routers import SimpleRouter, DefaultRouter

# 实例化路由类
router = DefaultRouter()

# 给路由注册视图集
router.register("student9", views.StudentViewSet, basename="student9")

# 把生成的路由列表和urlpatterns进行拼接组合
urlpatterns += router.urls