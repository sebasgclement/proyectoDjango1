from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


def index(request):
    title = 'Escuela de Formación Profesional de UNRaf'
    return render(request, "index.html",{
        'title':title
    })

def hello(request):
    return render(request, 'hello.html')

def about(request):
    return HttpResponse('<h2>Acerca de</h2>')

def project(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects':projects
    } )

def task(request):
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })



# Create your views here.
