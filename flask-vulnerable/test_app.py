
"""
@file test_app.py
@brief Pruebas unitarias de la aplicación Flask Vulnerable.

Este módulo contiene pruebas para verificar el comportamiento
del endpoint /hello.
"""

import unittest
from app import app


class FlaskAppTests(unittest.TestCase):
    """
    @brief Pruebas unitarias para los endpoints de la aplicación Flask.
    """

    def setUp(self):
        """
        @brief Prepara el cliente de pruebas antes de cada prueba.

        Crea un cliente de pruebas de Flask para realizar solicitudes
        HTTP sin iniciar un servidor externo.
        """
        self.client = app.test_client()

    def test_hello_endpoint_returns_200(self):
        """
        @brief Verifica que el endpoint /hello responda correctamente.

        Envía una solicitud GET con el parámetro name=Prueba y comprueba
        que la respuesta tenga código HTTP 200 y contenga el saludo esperado.
        """
        response = self.client.get("/hello?name=Prueba")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, Prueba!", response.data)


if __name__ == "__main__":
    """
    @brief Ejecuta las pruebas unitarias del módulo.
    """
    unittest.main()
