from django.contrib import admin
from .models import Schedule,Exercises,User

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Exercises)
admin.site.register(User)
