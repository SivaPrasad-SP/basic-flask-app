import unittest
from app import app, square

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, World!")

    def test_square_function(self):
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-4), 16)

    def test_square_route(self):
        response = self.app.get('/square/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Square of 5 is 25", response.data.decode())

if __name__ == '__main__':
    unittest.main()
