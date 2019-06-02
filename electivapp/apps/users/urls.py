from django.urls import path

from electivapp.apps.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_form_view,
    UsersHomeView,
    UserDeleteView
)

app_name = "users"
urlpatterns = [
    path("", view=UsersHomeView.as_view(), name="home"),
    path("list", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("create/", view=user_form_view, name="create"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("update/<str:username>", view=user_update_view, name="update"),
    path("delete/<int:pk>", view=UserDeleteView.as_view(), name="delete"),
]
