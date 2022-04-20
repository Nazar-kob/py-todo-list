from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from task.form import TaskForm
from task.models import Tag, Task


class TaskListView(generic.ListView):
    # https://prnt.sc/OUf8jy3LDelg
    model = Task


class TaskCreateView(generic.CreateView):
    # https://prnt.sc/u3uXWwNJ_TIB
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:home-page')


class TaskUpdateView(generic.UpdateView):
    # https://prnt.sc/wtVveh3O8wM5
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task:home-page')


class TaskDeleteView(generic.DeleteView):
    # https://prnt.sc/cMWeTxfByxLX
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task:home-page')


class TagsListView(generic.ListView):
    # https://prnt.sc/U7NLJyfCW2sJ
    model = Tag


class TagCreateView(generic.CreateView):
    # https://prnt.sc/agTKEqThBCJL
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tags-list")


class TagUpdateView(generic.UpdateView):
    # https://prnt.sc/ImP5_sr111qV
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tags-list")


class TagDeleteView(generic.DeleteView):
    # https://prnt.sc/a58TRsUU-RUa
    model = Tag
    template_name = 'task/tag_confirm_delete.html'
    success_url = reverse_lazy("task:tags-list")


def change_button_view(request, pk):
    # https://prnt.sc/2X5WDYvjhz4C
    button = Task.objects.get(id=pk)

    if button.is_done:
        button.is_done = False
    else:
        button.is_done = True

    button.save()

    return HttpResponseRedirect(reverse("taxi:home-page"))
