from django.contrib import admin
from .models import Alumno

# Register your models here.
@admin.register(Alumno)
class AdminAlumno(admin.ModelAdmin):
    list_per_page = 10000000000