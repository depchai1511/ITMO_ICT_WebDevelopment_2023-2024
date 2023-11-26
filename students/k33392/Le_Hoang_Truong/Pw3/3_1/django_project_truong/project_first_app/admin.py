from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Driver)
admin.site.register(models.Car)
admin.site.register(models.Ownership)
admin.site.register(models.DriverLicense)