from django.contrib import admin

from .models import EventoAuditorio

# Register your models here.
@admin.register(EventoAuditorio)
class AdminEvento(admin.ModelAdmin):
    list_per_page = 10000000000