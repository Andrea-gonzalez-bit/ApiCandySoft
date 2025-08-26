import unittest
from calificacion.models import Calificacion

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestCalificacion(unittest.TestCase):
    def test_crear_calificacion(self):

        try:
            calificacion = Calificacion.objects.create(
                puntuacion=2,  
                comentario="Bien, no hay quejas."
            )

            self.assertEqual(calificacion.puntuacion, 2)
            self.assertEqual(calificacion.get_puntuacion_display(), "Bien")
            self.assertEqual(calificacion.comentario, "Bien, no hay quejas.")

            print(f"{Colors.OKGREEN}✓ Calificación creada correctamente: {calificacion.get_puntuacion_display()}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Error al crear calificación: {e}{Colors.ENDC}")
            raise e

if __name__ == "__main__":
    unittest.main(verbosity=2)
