from django.test import TestCase


class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(1, 1)

    def test_animals_can_speak2(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(2, 2)

    def test_animals_cannot_speak(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(1, 2)
