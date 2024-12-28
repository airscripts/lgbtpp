import unittest
from lgbtpp.asexual import Asexual

class TestAsexual(unittest.TestCase):
    def setUp(self):
        self.asexual = Asexual()

    def test_get_name(self):
        self.assertEqual(self.asexual.get_name(), "Asexual")

    def test_get_description(self):
        self.assertIn("do not experience sexual attraction", self.asexual.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.asexual.get_wiki_url(), "ttps://lgbtqia.fandom.com/wiki/Asexuality")

if __name__ == '__main__':
    unittest.main()
