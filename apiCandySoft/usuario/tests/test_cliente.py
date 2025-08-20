import unittest
from usuario.models.usuario import Usuario
from usuario.models.cliente import Cliente
from rol.models import Rol

class Colors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class TestCliente(unittest.TestCase):
    def test_crear_cliente(self):

        try:
            rol_cliente, _ = Rol.objects.get_or_create(nombre="Cliente")

            usuario = Usuario.objects.create_user(
                username="Sofia_G",
                password="sofi109**",
                nombre="Sofia",
                apellido="Gallego",
                correo="sofi@example.com",
                rol_id=rol_cliente
            )

            cliente = Cliente.objects.create(
                usuario=usuario,
                nombre="Sofia",
                apellido="Gallego",
                tipo_documento="CC",
                numero_documento="106534567",
                correo="sofi@example.com",
                celular="3014794567"
            )

            self.assertEqual(cliente.nombre, "Sofia")
            self.assertEqual(cliente.apellido, "Gallego")
            self.assertEqual(cliente.correo, "sofi@example.com")
            self.assertEqual(usuario.username, "Sofia_G")


            print(f"{Colors.OKGREEN}✓ Cliente creado correctamente: {usuario.username}{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}✗ Error al crear cliente: {e}{Colors.ENDC}")
            raise e

if __name__ == "__main__":
    unittest.main(verbosity=2)
