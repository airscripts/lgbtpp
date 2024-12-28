import unittest
from lgbtpp.plus import Plus

class TestPlus(unittest.TestCase):
    def setUp(self):
        self.plus = Plus()

    def test_get_name(self):
        self.assertEqual(self.plus.get_name(), "Plus")

    def test_get_description(self):
        self.assertIn("stands for all", self.plus.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.plus.get_wiki_url(), "https://lgbtqia.fandom.com/")

if __name__ == '__main__':
    unittest.main()
