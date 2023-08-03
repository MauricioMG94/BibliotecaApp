from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import AutorViewSet, LibroViewSet, PaisViewSet

router = DefaultRouter()
router.register(r'autores_api', AutorViewSet, basename='autor')
router.register(r'libros_api', LibroViewSet, basename='libro')
router.register(r'paises_api', PaisViewSet, basename='pais')

urlpatterns = [
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear', views.crear_autor, name='crear_autor'),
    path('autores/<int:id>/editar', views.editar_autor, name='editar_autor'),
    path('autores/<int:id>/eliminar', views.eliminar_autor, name='eliminar_autor'),

    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear', views.crear_libro, name='crear_libro'),
    path('libros/<int:id>/editar', views.editar_libro, name='editar_libro'),
    path('libros/<int:id>/eliminar', views.eliminar_libro, name='eliminar_libro'),

    path('paises/', views.lista_paises, name='lista_paises'),
    path('paises/crear', views.crear_pais, name='crear_pais'),
    path('paises/<int:id>/editar', views.editar_pais, name='editar_pais'),
    path('paises/<int:id>/eliminar', views.eliminar_pais, name='eliminar_pais'),

    path('', include(router.urls)),
]
