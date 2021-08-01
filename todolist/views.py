from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def lists(request):
    all_tasks = Task.objects.all()
    count = 0
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lists')
    else:
        form = TaskForm()
    return render(request, 'todolist/list.html', {'all_tasks': all_tasks, 'form': form, 'count': count})


def delete_completed_task(request):
    Task.objects.filter(perfomed=True).delete()
    return redirect('lists')


def delete_all(request):
    Task.objects.all().delete()
    return redirect('lists')


def performed(request, performed_pk):
    task = Task.objects.get(pk=performed_pk)
    if task.perfomed == True:
        task.perfomed = False
        task.save()
    else:
        task.perfomed = True
        task.save()

    return redirect('lists')



