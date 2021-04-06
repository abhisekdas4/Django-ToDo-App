from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskModelForm

def index(request):
    tasks = TaskModel.objects.all()
    form = TaskModelForm()
    context = {
        'form': form,
        'tasks': tasks
    }

    if request.method == 'POST':
        form = TaskModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'task/index.html', context)


def update_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    form = TaskModelForm(instance=task)
    context = { 'form': form }

    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'task/update_task.html', context)


def delete_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    return render(request, 'task/delete.html', {'task':task})
