import unittest
from usuario.models.usuario import Usuario
from usuario.models.manicurista import Manicurista
from rol.models import Rol

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestManicurista(unittest.TestCase):
    def test_crear_manicurista(self):

        try:

            rol_manicurista, _ = Rol.objects.get_or_create(nombre="Manicurista")

            usuario = Usuario.objects.create_user(
                username="Fernanda_lo",
                password="fer234*",
                nombre="Fernanda",
                apellido="Lopez",
                correo="lopezfer@example.com",
                rol_id=rol_manicurista
            )

            manicurista = Manicurista.objects.create(
                usuario=usuario,
                nombre="Fernanda",
                apellido="Lopez",
                tipo_documento="CC",
                numero_documento="1032098667",
                correo="lopezfer@example.com",
                celular="3014587990",
                fecha_nacimiento="2001-10-13",
                fecha_contratacion="2023-05-20"
            )

            self.assertEqual(manicurista.nombre, "Fernanda")
            self.assertEqual(manicurista.apellido, "Lopez")
            self.assertEqual(manicurista.correo, "lopezfer@example.com")
            self.assertEqual(usuario.username, "Fernanda_lo")

            print(f"{Colors.OKGREEN}✓ Manicurista creado correctamente: {usuario.username}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Error al crear manicurista: {e}{Colors.ENDC}")
            raise e


if __name__ == "__main__":
    unittest.main(verbosity=2)
