from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask


def index(request):
    title = 'Escuela de Formación Profesional de UNRaf'
    return render(request, "index.html",{
        'title':title
    })

def hello(request):
    return render(request, 'hello.html')

def about(request):
    return render(request, "about.html")

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

"""
def create_task(request):
    print(request.GET)
    Task.objects.create(title=request.GET['title'], description=request.GET['description'], project_id=2)
    return render(request, "create_task.html", {
        'form':CreateNewTask() 
    })
"""
def create_task(request):
    if request.method == 'GET':
        return render(request, "create_task.html", {
            'form':CreateNewTask() 
        })    
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], project_id=2)
        return redirect('/task/')
        


# Create your views here.
