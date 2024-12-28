import unittest
from lgbtpp.bisexual import Bisexual

class TestBisexual(unittest.TestCase):
    def setUp(self):
        self.bisexual = Bisexual()

    def test_get_name(self):
        self.assertEqual(self.bisexual.get_name(), "Bisexual")

    def test_get_description(self):
        self.assertIn("multiple genders", self.bisexual.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.bisexual.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Bisexual")

if __name__ == '__main__':
    unittest.main()
