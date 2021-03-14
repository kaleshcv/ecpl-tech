from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(Cpu)
admin.site.register(Desktop)
admin.site.register(Assigned)
admin.site.register(ServiceCpu)
admin.site.register(ReturnCpu)