from django.urls import path

from .views import TiposActividadListView, TiposActividadFormView

app_name = "actividades"
urlpatterns = [
    path("tipos", view=TiposActividadListView.as_view(), name="lista_tipos"),
    path("tipos/crear", view=TiposActividadFormView.as_view(), name="nuevo_tipo"),
]
