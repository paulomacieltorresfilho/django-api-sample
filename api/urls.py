from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'person', views.PersonViewSet)
router.register(r'task', views.TaskViewSet)
router.register(r'tasktype', views.TaskTypeViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]