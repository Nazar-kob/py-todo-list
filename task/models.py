from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['name']


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(to=Tag, related_name='tasks')

    def __str__(self):
        return f"Content: {self.content} time {self.datetime}"

    class Meta:
        ordering = ['is_done', '-datetime']
