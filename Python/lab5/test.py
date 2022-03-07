import unittest
from Cake import Cake

class NameTestCase(unittest.TestCase):

    def setUp(self):
        self.Cake = Cake("Торт Дружба","Сметанный крем")

    def test_name(self):
        self.assertEqual(self.Cake.name, "Торт Дружба")

    def test_filling(self):
        self.assertEqual(self.Cake.filling, "Сметанный крем")

if __name__ == "__main__":
    unittest.main()
