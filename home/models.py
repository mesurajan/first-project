from django.db import models

# Create your models here.


class MonitorItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NetworkDevice(models.Model):
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProblemReport(models.Model):
    # Define fields for the ProblemReport model
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
