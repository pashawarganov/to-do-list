from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "-created"]

    def __str__(self):
        formatted_created = self.created.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.content} - {formatted_created}({self.done})"
