import unittest
from servicio.models import Servicio
from datetime import timedelta


class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class TestServicio(unittest.TestCase):
    def test_crear_servicio(self):

        try:
            servicio = Servicio.objects.create(
                nombre="Acrílicas",
                descripcion="Uñas resistentes y elegantes con acabado impecable.",
                precio=80.000,
                duracion=timedelta(minutes=60),
                url_imagen="https://i.pinimg.com/originals/d6/0f/4e/d60f4e89e6abf26bd6905787adda9fac.jpg"
            )

            self.assertEqual(servicio.nombre, "Acrílicas")
            self.assertEqual(servicio.precio, 80.000)
            self.assertEqual(servicio.duracion, timedelta(minutes=60))
            self.assertEqual(servicio.tipo, "Manicure") 

            print(f"{Colors.OKGREEN}✓ Servicio creado correctamente: {servicio.nombre}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Error al crear servicio: {e}{Colors.ENDC}")
            raise e


if __name__ == "__main__":
    unittest.main(verbosity=2)
