from django.urls import path

from .views import EventosListView, EventoFormView

app_name = "eventos"
urlpatterns = [
    path("", view=EventosListView.as_view(), name="home"),
    path("crear", view=EventoFormView.as_view(), name="crear"),
]
