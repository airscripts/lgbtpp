import unittest
from lgbtpp.agender import Agender

class TestAgender(unittest.TestCase):
    def setUp(self):
        self.agender = Agender()

    def test_get_name(self):
        self.assertEqual(self.agender.get_name(), "Agender")

    def test_get_description(self):
        self.assertIn("gender identity", self.agender.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.agender.get_wiki_url(), "https://lgbta.wikia.org/wiki/Agender")

if __name__ == '__main__':
    unittest.main()
