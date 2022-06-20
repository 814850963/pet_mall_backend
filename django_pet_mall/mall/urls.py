from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("stu", views.StudentModelViewSet, basename="stu"),

urlpatterns = [

] + router.urls