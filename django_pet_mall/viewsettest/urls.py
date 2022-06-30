from django.contrib import admin
from django.urls import path, include, re_path
from. import views

urlpatterns = [
    path('students/', views.StudentAPIView.as_view()),
    path('students1/', views.StudentMixinView.as_view()),
    re_path("^students3/(?P<pk>\d+)/$}", views.StudentInfoMixinView.as_view())


]
