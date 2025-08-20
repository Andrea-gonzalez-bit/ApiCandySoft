import unittest
from rol.models import Rol

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestRol(unittest.TestCase):
    def test_crear_rol(self):
        try:
            rol, created = Rol.objects.get_or_create(
                nombre="Aseador",
                defaults={"descripcion": "Hace aseo y ya"}
            )

            if created:
                print(f"{Colors.OKGREEN}✓ Rol creado correctamente: {rol.nombre}{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}✗ El rol '{rol.nombre}' ya existe, no se puede volver a crear.{Colors.ENDC}")

            self.assertEqual(rol.nombre, "Aseador")
            self.assertEqual(rol.descripcion, "Hace aseo y ya")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Error al crear rol: {e}{Colors.ENDC}")
            raise e

if __name__ == "__main__":
    unittest.main(verbosity=2)
