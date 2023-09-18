from django.contrib import admin
from .models import Server, NetworkDevice, ProblemReport

admin.site.register(Server)
admin.site.register(NetworkDevice)
admin.site.register(ProblemReport)
