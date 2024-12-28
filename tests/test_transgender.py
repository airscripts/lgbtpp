import unittest
from lgbtpp.transgender import Transgender

class TestTransgender(unittest.TestCase):
    def setUp(self):
        self.transgender = Transgender()

    def test_get_name(self):
        self.assertEqual(self.transgender.get_name(), "Transgender")

    def test_get_description(self):
        self.assertIn("umbrella term", self.transgender.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.transgender.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Transgender")

if __name__ == '__main__':
    unittest.main()
