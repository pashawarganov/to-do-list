from django.urls import path

from to_do_list.views import TaskListView


urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
]

app_name = "to_do_list"
