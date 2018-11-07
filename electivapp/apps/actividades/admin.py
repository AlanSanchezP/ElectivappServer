from django.contrib import admin
from .models import TipoActividad

# Register your models here.
@admin.register(TipoActividad)
class AdminTipoActividad(admin.ModelAdmin):
    list_per_page = 10000000000