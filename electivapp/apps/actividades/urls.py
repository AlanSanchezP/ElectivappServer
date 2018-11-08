from django.urls import path

from .views import TiposActividadListView, TiposActividadFormView, TiposActividadUpdateView, TiposActividadDeleteView, RegistrarActividadView

app_name = "actividades"
urlpatterns = [
    path("tipos", view=TiposActividadListView.as_view(), name="lista_tipos"),
    path("tipos/crear", view=TiposActividadFormView.as_view(), name="nuevo_tipo"),
    path("tipos/modificar/<str:pk>", view=TiposActividadUpdateView.as_view(), name="modificar_tipo"),
    path("tipos/eliminar/<str:pk>", view=TiposActividadDeleteView.as_view(), name="eliminar_tipo"),
    path("registrar", view=RegistrarActividadView.as_view(), name="registrar"),
]
