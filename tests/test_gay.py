import unittest
from lgbtpp.gay import Gay

class TestGay(unittest.TestCase):
    def setUp(self):
        self.gay = Gay()

    def test_get_name(self):
        self.assertEqual(self.gay.get_name(), "Gay")

    def test_get_description(self):
        self.assertIn("enduring physical", self.gay.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.gay.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Gay")

if __name__ == '__main__':
    unittest.main()
