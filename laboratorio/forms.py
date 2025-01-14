from django import forms  # Importa la funcionalidad de formularios de Django
from .models import Laboratorio  # Importa el modelo Laboratorio definido en models.py


# Clase que define un formulario basado en el modelo Laboratorio
class LaboratorioForm(forms.ModelForm):
    # Clase interna Meta para configurar el formulario
    class Meta:
        # Especifica que este formulario está vinculado al modelo Laboratorio
        model = Laboratorio
        # Define los campos del modelo que estarán disponibles en el formulario
        fields = ["nombre", "ciudad", "pais"]
