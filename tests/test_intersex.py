import unittest
from lgbtpp.intersex import Intersex

class TestIntersex(unittest.TestCase):
    def setUp(self):
        self.intersex = Intersex()

    def test_get_name(self):
        self.assertEqual(self.intersex.get_name(), "Intersex")

    def test_get_description(self):
        self.assertIn("umbrella term", self.intersex.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.intersex.get_wiki_url(), "ttps://lgbtqia.fandom.com/wiki/Intersex")

if __name__ == '__main__':
    unittest.main()
