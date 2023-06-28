import unittest
from translator import french_to_english

class TranslatorTestCase(unittest.TestCase):
    def test_french_to_english(self):
        translation = french_to_english("Bonjour")
        self.assertEqual(translation, "Hello")
        self.assertNotEqual(translation, "Bonjour")

if __name__ == '__main__':
    unittest.main()

import unittest
from translator import english_to_french

class TranslatorTestCase(unittest.TestCase):
    def test_english_to_french(self):
        translation = english_to_french("Hello")
        self.assertEqual(translation, "Bonjour")
        self.assertNotEqual(translation, "Hello")

if __name__ == '__main__':
    unittest.main()
