from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from to_do_list.models import Task, Tag


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 3


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:index")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list:index")


class TagListView(ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tag_list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do_list:tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do_list:tag_list")


def task_toggle_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do_list:index"))
