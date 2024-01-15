#import sys
#sys.path.append("../")
from hw4 import *
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from datetime import date
import unittest


class TestPatient(unittest.TestCase):
    
    def test_patient_add_test(self):
        person = Patient('angelo', ['fever', 'cough'])
        person.add_test('covid', True)
        tests = {'covid': True}
        self.assertDictEqual(tests, person.tests)
        
    def test_patient_has_covid_no_covid_without_test(self):
        person = Patient('angelo', ['fever', 'cough'])
        self.assertEqual(person.has_covid(), 0.25)

    def test_patient_has_covid_no_covid_with_test(self):
        person = Patient('angelo', ['fever', 'cough'])
        person.add_test('covid', False)
        self.assertEqual(person.has_covid(), 0.01)

    def test_patient_has_covid_yes_covid(self):
        person = Patient('angelo', ['fever', 'cough'])
        person.add_test('covid', True)
        self.assertEqual(person.has_covid(), 0.99)


class TestCardAndDeck(unittest.TestCase):

    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_draw(self):
        my_deck = Deck()
        my_deck.draw()
        self.assertEqual(len(my_deck.cards), 51)

    def test_draw_all_cards(self):
        deck = Deck()
        for _ in range(52):
            deck.draw()
        deck.draw()  # attempting to draw from an empty deck
        self.assertEqual(len(deck.cards), 0)

    def test_deck_shuffle(self):
        deck = Deck()
        initial_order = deck.cards[:]
        deck.shuffle()
        shuffled_order = deck.cards
        self.assertNotEqual(initial_order, shuffled_order)


class TestFigures(unittest.TestCase):

    def test_triangle_compute_perimeter(self):
        shape = Triangle(5, 6, 7, 5)
        self.assertEqual(shape.compute_perimeter(), 18)

    def test_triangle_compute_surface(self):
        shape = Triangle(5, 6, 7, 5)
        self.assertEqual(shape.compute_surface(), 12.5)

    def test_rectangle_compute_perimeter(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.compute_perimeter(), 22)

    def test_rectangle_compute_surface(self):
        shape = Rectangle(5, 6)
        self.assertEqual(shape.compute_surface(), 30)

    def test_circle_compute_perimeter(self):
        shape = Circle(5)
        self.assertEqual(shape.compute_perimeter(), 31.41592653589793)

    def test_circle_compute_surface(self):
        shape = Circle(5)
        self.assertEqual(shape.compute_surface(), 78.53981633974483)


if __name__ == '__main__':
    unittest.main()
