from django.db import models


class MonitorItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class ProblemReport(models.Model):
    TYPE_CHOICES = [
        ("Ambulance", "Ambulance"),
        ("Other", "Other"),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} Problem - {self.timestamp}"
