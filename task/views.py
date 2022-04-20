
from django.urls import reverse_lazy
from django.views import generic

from task.form import TaskForm
from task.models import Tag, Task


class TaskListView(generic.ListView):
    # https://prnt.sc/eZwGA5CdwMNO
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

