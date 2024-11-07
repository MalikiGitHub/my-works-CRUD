from django.contrib import admin

from .models import Tags, Categories, Blog

# Register your models here.
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Categories)