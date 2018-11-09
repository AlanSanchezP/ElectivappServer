from django.urls import path

from electivapp.apps.alumnos.views import AlumnosListView, ResponsablesListView, ResponsableFormView, ResponsableUpdateView, ResponsableDeleteView

app_name = "alumnos"
urlpatterns = [
    path("consulta", view=AlumnosListView.as_view(), name="lista"),
    path("responsables", view=ResponsablesListView.as_view(), name="lista_responsables"),
    path("responsables/crear", view=ResponsableFormView.as_view(), name="nuevo_responsable"),
    path("responsables/modificar/<str:pk>", view=ResponsableUpdateView.as_view(), name="modificar_responsable"),
    path("responsables/eliminar/<str:pk>", view=ResponsableDeleteView.as_view(), name="eliminar_responsable"),
]
