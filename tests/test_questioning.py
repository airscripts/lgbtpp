import unittest
from lgbtpp.questioning import Questioning

class TestQuestioning(unittest.TestCase):
    def setUp(self):
        self.questioning = Questioning()

    def test_get_name(self):
        self.assertEqual(self.questioning.get_name(), "Questioning")

    def test_get_description(self):
        self.assertIn("exploring", self.questioning.get_description())

    def test_get_wiki_url(self):
        self.assertEqual(self.questioning.get_wiki_url(), "https://lgbtqia.fandom.com/wiki/Questioning")

if __name__ == '__main__':
    unittest.main()
