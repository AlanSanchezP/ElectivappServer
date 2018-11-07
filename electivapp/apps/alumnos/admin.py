from django.contrib import admin
from .models import Alumno, Responsable

# Register your models here.
@admin.register(Alumno)
class AdminAlumno(admin.ModelAdmin):
    list_per_page = 10000000000

@admin.register(Responsable)
class AdminResponsable(admin.ModelAdmin):
    list_display = ('alumno',)
    list_per_page = 10000000000