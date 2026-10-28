
import unittest
from app import app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello_endpoint_returns_200(self):
        response = self.client.get("/hello?name=Prueba")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, Prueba!", response.data)


if __name__ == "__main__":
    unittest.main()
