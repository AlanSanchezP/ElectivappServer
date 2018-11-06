from django.urls import path

from . import views

app_name = "actividades"
urlpatterns = [
    path("", view=views.Test.as_view(), name="test"),
]
