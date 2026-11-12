import unittest
from app import mensaje

class TestApp(unittest.TestCase):
    def test_mensaje(self):
        self.assertEqual(mensaje(), "Hola Mundo desde DevSecOps!")
        
if __name__ == '__main__':
    unittest.main()
