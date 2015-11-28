from django.contrib import admin
from .models import HomeWorkModel

# Register your models here.
class HomeWorkModelAdmin(admin.ModelAdmin):
    list_display = ('desc','tag')

admin.site.register(HomeWorkModel,HomeWorkModelAdmin)
