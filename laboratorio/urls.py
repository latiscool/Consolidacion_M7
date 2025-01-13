from django.urls import path
from . import views

urlpatterns = [
    path("", views.laboratorio_list, name="laboratorio_list"),
    path("<int:pk>/", views.laboratorio_detail, name="laboratorio_detail"),
    path("new/", views.laboratorio_new, name="laboratorio_new"),
    path("<int:pk>/edit/", views.laboratorio_edit, name="laboratorio_edit"),
    path("<int:pk>/delete/", views.laboratorio_delete, name="laboratorio_delete"),
]
