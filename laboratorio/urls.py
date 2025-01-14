from django.urls import path  # Importa la función 'path' para definir rutas de URL
from . import views  # Importa las vistas de la aplicación 'laboratorio'

# Lista de rutas URL para la aplicación 'laboratorio'
urlpatterns = [
    # Ruta para listar todos los laboratorios
    # URL: "/" (raíz de la aplicación)
    # Vista asociada: laboratorio_list
    # Nombre de la URL: "laboratorio_list"
    path("", views.laboratorio_list, name="laboratorio_list"),
    # Ruta para mostrar los detalles de un laboratorio específico
    # URL: "/<int:pk>/" (donde <int:pk> es el ID del laboratorio)
    # Vista asociada: laboratorio_detail
    # Nombre de la URL: "laboratorio_detail"
    path("<int:pk>/", views.laboratorio_detail, name="laboratorio_detail"),
    # Ruta para crear un nuevo laboratorio
    # URL: "/new/"
    # Vista asociada: laboratorio_new
    # Nombre de la URL: "laboratorio_new"
    path("new/", views.laboratorio_new, name="laboratorio_new"),
    # Ruta para editar un laboratorio existente
    # URL: "/<int:pk>/edit/" (donde <int:pk> es el ID del laboratorio a editar)
    # Vista asociada: laboratorio_edit
    # Nombre de la URL: "laboratorio_edit"
    path("<int:pk>/edit/", views.laboratorio_edit, name="laboratorio_edit"),
    # Ruta para eliminar un laboratorio existente
    # URL: "/<int:pk>/delete/" (donde <int:pk> es el ID del laboratorio a eliminar)
    # Vista asociada: laboratorio_delete
    # Nombre de la URL: "laboratorio_delete"
    path("<int:pk>/delete/", views.laboratorio_delete, name="laboratorio_delete"),
]
