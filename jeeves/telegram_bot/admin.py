from django.contrib import admin
from .models import HomeWorkModel

# Register your models here.
class HomeWorkModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(HomeWorkModel,HomeWorkModelAdmin)
