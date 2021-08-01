from django.urls import path
from .views import lists, performed, delete_completed_task, delete_all

urlpatterns = [
    path('', lists, name='lists'),
    path('delete_completed_task/', delete_completed_task, name='delete_completed_task'),
    path('delete_all/', delete_all, name='delete_all'),
    path('performed/<int:performed_pk>/', performed, name='performed'),
]
