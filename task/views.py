from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from task.form import TaskForm
from task.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:home-page')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:home-page')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task:home-page')


class TagsListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'task/tag_confirm_delete.html'
    success_url = reverse_lazy("task:tags-list")


def change_button_view(request, pk):
    button = Task.objects.get(id=pk)

    if button.is_done:
        button.is_done = False
    else:
        button.is_done = True

    button.save()

    return HttpResponseRedirect(reverse("taxi:home-page"))
