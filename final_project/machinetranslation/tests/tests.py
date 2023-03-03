import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def testEnToFr(self):
        self.assertNotEqual(english_to_french('None'), ' ')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def testFrToEn(self):
        self.assertNotEqual(french_to_english('None'), ' ')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()