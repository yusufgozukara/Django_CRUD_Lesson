from django.urls import path

from .views import index, student_list

urlpatterns = [

    path('', index, name='index'),
    path('list/', student_list, name='list'),
]