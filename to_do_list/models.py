from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)
    deadline_date_time = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "-date_time"]

    def __str__(self):
        return f"{self.content} - {self.date_time}({self.done})"
