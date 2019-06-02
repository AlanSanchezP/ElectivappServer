from django.urls import path
from django.contrib.auth.views import password_change

from electivapp.apps.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_form_view,
    user_pass_view,
)

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("create/", view=user_form_view, name="create"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("pass", view=user_pass_view, name="pass")
]
