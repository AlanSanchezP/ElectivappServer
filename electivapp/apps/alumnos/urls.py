from django.urls import path

from electivapp.apps.alumnos.views import AlumnosListView

app_name = "alumnos"
urlpatterns = [
    path("consulta", view=AlumnosListView.as_view(), name="lista"),
]
