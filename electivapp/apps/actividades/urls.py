from django.urls import path

from .views import (
    ActividadesHomeView, 
    TiposActividadListView, 
    TiposActividadFormView, 
    TiposActividadUpdateView, 
    TiposActividadDeleteView, 
    RegistrarActividadView, 
    CorregirActividadView,
    CategoriasListView,
    CategoriasFormView,
    CategoriasUpdateView,
    CategoriasDeleteView
)

app_name = "actividades"
urlpatterns = [
    path("", view=ActividadesHomeView.as_view(), name="home"),
    path("tipos", view=TiposActividadListView.as_view(), name="lista_tipos"),
    path("tipos/crear", view=TiposActividadFormView.as_view(), name="nuevo_tipo"),
    path("tipos/modificar/<str:pk>", view=TiposActividadUpdateView.as_view(), name="modificar_tipo"),
    path("tipos/eliminar/<str:pk>", view=TiposActividadDeleteView.as_view(), name="eliminar_tipo"),
    path("registrar", view=RegistrarActividadView.as_view(), name="registrar"),
    path("registrar/error", view=CorregirActividadView.as_view(), name="corregir"),
    path("categorias", view=CategoriasListView.as_view(), name="categorias"),
    path("categorias/crear", view=CategoriasFormView.as_view(), name="nueva_categoria"),
    path("categorias/modificar/<str:pk>", view=CategoriasUpdateView.as_view(), name="modificar_categoria"),
    path("categorias/eliminar/<str:pk>", view=CategoriasDeleteView.as_view(), name="eliminar_categoria"),
    
]
