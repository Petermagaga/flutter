from  django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TaskListCreate,TaskDetail


router=DefaultRouter()
router.register(r'tasks',TaskViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path ('api/tasks',TaskListCreate.as_view(),name='task-list'),
    path('api/tasks/<int:pk>/',TaskDetail.as_view(),name='task-detail'),
]