from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("stu", views.StudentModelViewSet, basename="stu"),

urlpatterns = [
    path('index', views.index)
] + router.urls