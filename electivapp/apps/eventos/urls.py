from django.urls import path

from electivapp.apps.actividades import views

app_name = "eventos"
urlpatterns = [
    path("", view=views.Test.as_view(), name="home"),
]
