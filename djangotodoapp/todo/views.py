from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from .models import Todo
from django.http import FileResponse
import os
from django.conf import settings
# Create your views here.

def index(request):
    context = {
        "number" : 10,
        "numbers" : [1,2,3,4,5,6,7,8,9]
    }

    todos = Todo.objects.all()

    return render(request,"index.html",{"todos":todos})

def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get("title")
        newTodo = Todo(title=title,completed = False)
        newTodo.save()
        return redirect("/")
    
def update(request,id):
    #todo = Todo.objects.filter(id=id).first()
    todo = get_object_or_404(Todo,id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("/")

def delete(request,id):
    #todo = Todo.objects.filter(id=id).first()
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect("/")

def download_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'python-3.12.3-amd64.exe')
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="python-3.12.3-amd64.exe"'
    return response