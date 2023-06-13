from django.contrib import admin

# Register your models here.
from .models import About, Intro, Service

admin.site.register(About)
admin.site.register(Intro)
admin.site.register(Service)