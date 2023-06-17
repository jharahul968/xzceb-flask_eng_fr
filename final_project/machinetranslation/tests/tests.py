import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')