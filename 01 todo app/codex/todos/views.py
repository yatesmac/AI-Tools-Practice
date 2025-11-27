from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone

from .forms import TodoForm
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    form = TodoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Todo created successfully.")
        return redirect("home")

    today = timezone.localdate()
    return render(
        request,
        "home.html",
        {
            "form": form,
            "todos": todos,
            "today": today,
        },
    )


def edit(request, pk: int):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Todo updated.")
        return redirect("home")

    return render(request, "home.html", {"form": form, "editing": True, "todo": todo, "todos": Todo.objects.all()})


def toggle_resolved(request, pk: int):
    todo = get_object_or_404(Todo, pk=pk)
    todo.resolved = not todo.resolved
    todo.save()
    messages.info(
        request,
        f"Marked '{todo.title}' as {'done' if todo.resolved else 'pending'}.",
    )
    return redirect("home")


def delete(request, pk: int):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        todo.delete()
        messages.warning(request, "Todo deleted.")
        return redirect("home")
    return render(request, "confirm_delete.html", {"todo": todo})
