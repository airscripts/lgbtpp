import unittest
from lgbtpp.two_spirit import TwoSpirit

class TestTwoSpirit(unittest.TestCase):
    def setUp(self):
        self.two_spirit = TwoSpirit()

    def test_get_name(self):
        self.assertEqual(self.two_spirit.get_name(), "Two-Spirit")

    def test_get_description(self):
        self.assertIn("Native identity", self.two_spirit.get_description())
        self.assertIn("gender", self.two_spirit.get_description())
        self.assertIn("spiritual", self.two_spirit.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.two_spirit.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Two-Spirit")

if __name__ == '__main__':
    unittest.main()
