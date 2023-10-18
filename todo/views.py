from django.shortcuts import get_object_or_404, render, redirect
from .models import Task


# Create your views here.
def add_task(request):
    name = request.POST["task"]
    Task.objects.create(name=name)
    return redirect("home")


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk, is_completed=False)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk, is_completed=True)
    task.is_completed = False
    task.save()
    return redirect("home")


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, is_completed=False)
    if request.method == "POST":
        new_task_name = request.POST["task"]
        task.name = new_task_name
        task.save()
        return redirect("home")
    else:
        context = {
            "task": task,
        }
        return render(request, "edit-task.html", context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, is_completed=False)
    task.delete()
    return redirect("home")
