from django.urls import path

from electivapp.apps.alumnos.views import AlumnosSearchView, AlumnoUpdateView, ResponsablesListView, ResponsableFormView, ResponsableUpdateView, ResponsableDeleteView, ResponsablePasswordView

app_name = "alumnos"
urlpatterns = [
    path("consulta", view=AlumnosSearchView.as_view(), name="consulta"),
    path("corregir/<int:pk>", view=AlumnoUpdateView.as_view(), name="corregir"),
    path("responsables", view=ResponsablesListView.as_view(), name="lista_responsables"),
    path("responsables/crear", view=ResponsableFormView.as_view(), name="nuevo_responsable"),
    path("responsables/modificar/<int:pk>", view=ResponsableUpdateView.as_view(), name="modificar_responsable"),
    path("responsables/eliminar/<int:pk>", view=ResponsableDeleteView.as_view(), name="eliminar_responsable"),
    path("responsables/cambiarpassword/<int:pk>", view=ResponsablePasswordView.as_view(), name="password_responsable"),
]
