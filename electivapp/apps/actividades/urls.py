from django.urls import path

from .views import TiposActividadListView

app_name = "actividades"
urlpatterns = [
    path("", view=TiposActividadListView.as_view(), name="tipos")
]
