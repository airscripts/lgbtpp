import unittest
from lgbtpp.lesbian import Lesbian

class TestLesbian(unittest.TestCase):
    def setUp(self):
        self.lesbian = Lesbian()

    def test_get_name(self):
        self.assertEqual(self.lesbian.get_name(), "Lesbian")

    def test_get_description(self):
        self.assertIn("woman who is attracted", self.lesbian.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.lesbian.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Lesbian")

if __name__ == '__main__':
    unittest.main()
