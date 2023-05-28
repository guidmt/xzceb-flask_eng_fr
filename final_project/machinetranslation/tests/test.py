import unittest

from translator import eng_to_fr, fr_to_eng

class fr_to_eng_test(unittest.TestCase):
    def test_is_not_null(self):
        self.assertNotEqual(fr_to_eng("Bonjour"),"")
    def test_translation(self):
        self.assertEqual(fr_to_eng("Bonjour"), "Hello")

class eng_to_fr_test(unittest.TestCase):
    def test_is_not_null(self):
        self.assertNotEqual(eng_to_fr("Hello"), "")
    def test_translation(self):
        self.assertEqual(eng_to_fr("Hello"), "Bonjour")

unittest.main()
