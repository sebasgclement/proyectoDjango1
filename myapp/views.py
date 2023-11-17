from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
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
    return render(request, 'project/projects.html',{
        'projects':projects
    } )

def task(request):
    tasks = Task.objects.all()
    return render(request, 'task/task.html', {
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
        return render(request, "task/create_task.html", {
            'form':CreateNewTask() 
        })    
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project= request.POST['project_id'])
        return redirect('task')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create_project.html', {
        'form' : CreateNewProject
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('project')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'project/detail.html', {
        'project': project,
        'tasks': tasks
    })
        



