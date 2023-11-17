from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('project/<int:id>', views.project_detail, name='project_detail'),
    path('task/', views.task, name='task'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')
]