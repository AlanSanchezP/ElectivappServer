from django.urls import path

from .views import EventosListView

app_name = "eventos"
urlpatterns = [
    path("", view=EventosListView.as_view(), name="home"),
]
