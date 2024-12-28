import unittest
from lgbtpp.queer import Queer

class TestQueer(unittest.TestCase):
    def setUp(self):
        self.queer = Queer()

    def test_get_name(self):
        self.assertEqual(self.queer.get_name(), "Queer")

    def test_get_description(self):
        self.assertIn("identifier", self.queer.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.queer.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Queer")

if __name__ == '__main__':
    unittest.main()
