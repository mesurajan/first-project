from django.db import models


class InfrastructureProject(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    progress = models.PositiveIntegerField(default=0)
    cost = models.CharField(max_length=100)
    development_period = models.CharField(max_length=100)
    completion_time = models.CharField(max_length=100)

    def __str__(self):
        return self.name
