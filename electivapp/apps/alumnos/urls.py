from django.urls import path

from electivapp.apps.alumnos.views import AlumnosListView, ResponsablesListView

app_name = "alumnos"
urlpatterns = [
    path("consulta", view=AlumnosListView.as_view(), name="lista"),
    path("responsables", view=ResponsablesListView.as_view(), name="lista_responsables"),
]
