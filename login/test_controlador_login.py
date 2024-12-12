import unittest
from controlador_login import ControladorLogin


class TestControladorLogin(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorLogin()

    def test_login_sucesso(self):
        resultado = self.controlador.login("senha123")
        self.assertEqual(resultado, "Login bem-sucedido!")

    def test_tres_tentativas_incorretas(self):
        for _ in range(1):
            self.controlador.login("senhaErrada")
        resultado = self.controlador.login("senhaErrada")
        self.assertEqual(resultado, "Usuário bloqueado após 3 tentativas incorretas.")


if __name__ == "__main__":
    unittest.main()
