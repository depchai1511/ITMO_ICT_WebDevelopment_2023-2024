from django.contrib import admin
from .models import User,Conference,ConferenceTopic,Topic,Registration,Comment,PresentationResult


# Register your models here.
admin.site.register(User)
admin.site.register(Conference)
admin.site.register(ConferenceTopic)
admin.site.register(Topic)
admin.site.register(Registration)
admin.site.register(Comment)
admin.site.register(PresentationResult)
