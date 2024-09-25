from django.shortcuts import render
from django.views.generic import ListView

from to_do_list.models import Task


class TaskListView(ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
