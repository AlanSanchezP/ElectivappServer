from django.urls import path

from .views import EventosListView, EventoFormView, EventoUpdateView, EventoDeleteView

app_name = "eventos"
urlpatterns = [
    path("", view=EventosListView.as_view(), name="home"),
    path("crear", view=EventoFormView.as_view(), name="crear"),
    path("modificar/<str:pk>", view=EventoUpdateView.as_view(), name="modificar"),
    path("eliminar/<str:pk>", view=EventoDeleteView.as_view(), name="eliminar"),
]
