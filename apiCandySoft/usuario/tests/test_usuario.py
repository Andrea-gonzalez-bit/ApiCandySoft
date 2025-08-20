import unittest
from usuario.models.usuario import Usuario
from rol.models import Rol

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestUsuario(unittest.TestCase):
    def test_crear_usuario(self):

        try:

            rol_Recepcionista, _ = Rol.objects.get_or_create(nombre="Recepcionista")

            usuario = Usuario.objects.create_user(
                username="Caro_M",
                password="morales123**",
                nombre="Carolina",
                apellido="Morales",
                correo="caromor@example.com",
                tipo_documento="CC",
                numero_documento="1103457687",
                rol_id=rol_Recepcionista
            )

            self.assertEqual(usuario.nombre, "Carolina")
            self.assertEqual(usuario.apellido, "Morales")
            self.assertEqual(usuario.correo, "caromor@example.com")
            self.assertEqual(usuario.username, "Caro_M")

            print(f"{Colors.OKGREEN}✓ Usuario creado correctamente: {usuario.username}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Error al crear usuario: {e}{Colors.ENDC}")
            raise e


if __name__ == "__main__":
    unittest.main(verbosity=2)
