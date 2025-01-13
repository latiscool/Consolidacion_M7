from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio


# Clase para probar el modelo Laboratorio
class LaboratorioModelTest(TestCase):
    # Método de configuración inicial: se ejecuta una sola vez antes de todas las pruebas de esta clase
    @classmethod
    def setUpTestData(cls):
        # Crea un laboratorio de prueba en la base de datos temporal
        Laboratorio.objects.create(
            nombre="Lab Test", ciudad="Ciudad Test", pais="País Test"
        )

    # Prueba que los campos del modelo contengan los valores correctos
    def test_laboratorio_content(self):
        # Obtiene el laboratorio creado en setUpTestData por su ID
        laboratorio = Laboratorio.objects.get(id=1)
        # Verifica que el campo 'nombre' sea igual al valor esperado
        self.assertEqual(laboratorio.nombre, "Lab Test")
        # Verifica que el campo 'ciudad' sea igual al valor esperado
        self.assertEqual(laboratorio.ciudad, "Ciudad Test")
        # Verifica que el campo 'pais' sea igual al valor esperado
        self.assertEqual(laboratorio.pais, "País Test")
        # Mensaje descriptivo en la consola si la prueba pasa correctamente
        print(
            "✔ Modelo: test_laboratorio_content pasó correctamente. Los campos 'nombre', 'ciudad' y 'pais' tienen los valores esperados."
        )


# Clase para probar las vistas relacionadas con Laboratorio
class LaboratorioViewTest(TestCase):
    # Método de configuración inicial: se ejecuta una sola vez antes de todas las pruebas de esta clase
    @classmethod
    def setUpTestData(cls):
        # Crea un laboratorio de prueba en la base de datos temporal
        Laboratorio.objects.create(
            nombre="Lab Test", ciudad="Ciudad Test", pais="País Test"
        )

    # Prueba que la URL raíz ('/') exista y sea accesible
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/")  # Realiza una solicitud GET a la URL raíz ('/')
        self.assertEqual(
            response.status_code, 200
        )  # Verifica que el código de estado HTTP sea 200 (OK)
        print(
            "✔ Vista: test_view_url_exists_at_desired_location pasó correctamente. La URL '/' es accesible (status code 200)."
        )

    # Prueba que la vista sea accesible usando el nombre de la URL 'laboratorio_list'
    def test_view_url_accessible_by_name(self):
        response = self.client.get(
            reverse("laboratorio_list")
        )  # Genera la URL usando el nombre 'laboratorio_list'
        self.assertEqual(
            response.status_code, 200
        )  # Verifica que el código de estado HTTP sea 200 (OK)
        print(
            "✔ Vista: test_view_url_accessible_by_name pasó correctamente. La vista 'laboratorio_list' es accesible por su nombre."
        )

    # Prueba que la vista utilice el template correcto ('laboratorio_list.html')
    def test_view_uses_correct_template(self):
        response = self.client.get(
            reverse("laboratorio_list")
        )  # Genera la URL usando el nombre 'laboratorio_list'
        self.assertEqual(
            response.status_code, 200
        )  # Verifica que el código de estado HTTP sea 200 (OK)
        self.assertTemplateUsed(
            response, "laboratorio_list.html"
        )  # Verifica que se use el template correcto
        print(
            "✔ Vista: test_view_uses_correct_template pasó correctamente. Se está usando el template 'laboratorio_list.html'."
        )

    # Prueba que la lista de laboratorios devuelva todos los registros creados y contenga datos esperados
    def test_list_all_laboratorios(self):
        response = self.client.get(
            reverse("laboratorio_list")
        )  # Genera la URL usando el nombre 'laboratorio_list'
        self.assertEqual(
            response.status_code, 200
        )  # Verifica que el código de estado HTTP sea 200 (OK)
        self.assertTrue(
            len(response.context["laboratorios"]) == 1
        )  # Verifica que haya exactamente un laboratorio en la lista
        self.assertContains(
            response, "Lab Test"
        )  # Verifica que el contenido devuelto contenga "Lab Test"
        print(
            "✔ Vista: test_list_all_laboratorios pasó correctamente. La lista contiene todos los laboratorios creados."
        )
