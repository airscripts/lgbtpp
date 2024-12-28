import unittest
from lgbtpp.aromantic import Aromantic

class TestAromantic(unittest.TestCase):
    def setUp(self):
        self.aromantic = Aromantic()

    def test_get_name(self):
        self.assertEqual(self.aromantic.get_name(), "Aromantic")

    def test_get_description(self):
        self.assertIn("do not experience romantic attraction", self.aromantic.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.aromantic.get_wiki_url(), "https://lgbta.wikia.org/wiki/Aromantic")

if __name__ == '__main__':
    unittest.main()
