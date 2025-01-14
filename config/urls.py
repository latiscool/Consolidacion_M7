"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import (
    admin,
)  # Importa las herramientas para registrar y gestionar el panel administrativo de Django
from django.urls import (
    path,
    include,
)  # Importa funciones para definir rutas URL y "incluir" rutas de otras aplicaciones

# Lista de rutas URL principales del proyecto
urlpatterns = [
    # Ruta para acceder al panel administrativo
    # URL: "/admin/"
    # Vista asociada: admin.site.urls (gestiona automáticamente el panel administrativo)
    path("admin/", admin.site.urls),
    # Ruta principal para la aplicación "laboratorio"
    # URL: "/" (raíz del sitio web)
    # Incluye todas las rutas definidas en laboratorio/urls.py
    path("", include("laboratorio.urls")),
]
