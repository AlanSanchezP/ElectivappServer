from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from electivapp.apps.users.views import HomepageView
from electivapp.apps.alumnos.api import CarrerasListAPI, CustomAuthToken
from electivapp.apps.eventos.api import EventosListAPI, RegistrarAsistenciaQRAPI

urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("electivapp.apps.users.urls", namespace="users"),
    ),
    path(
        "actividades/",
        include("electivapp.apps.actividades.urls", namespace="actividades"),
    ),
    path(
        "alumnos/",
        include("electivapp.apps.alumnos.urls", namespace="alumnos"),
    ),
    path(
        "eventos/",
        include("electivapp.apps.eventos.urls", namespace="eventos"),
    ),
    path("accounts/", include("allauth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/eventos", view=EventosListAPI.as_view()),
    path("api/carreras", view=CarrerasListAPI.as_view()),
    path("api/token-auth/", view=CustomAuthToken.as_view()),
    path("api/eventos/asistencia/qr", view=RegistrarAsistenciaQRAPI.as_view()),
    # Your stuff: custom urls includes go here
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
