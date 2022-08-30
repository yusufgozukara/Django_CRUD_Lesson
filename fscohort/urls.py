from django.urls import path

from .views import index, student_list, student_add

urlpatterns = [

    path('', index, name='index'),
    path('list/', student_list, name='list'),
    path('add/', student_add, name='add'),

]