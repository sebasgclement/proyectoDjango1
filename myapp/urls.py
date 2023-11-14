from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('hello/', views.hello),
    path('about/', views.about),
    path('project/', views.project),
    path('task/', views.task),
    path('create_task/', views.create_task)
]