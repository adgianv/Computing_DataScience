import random
from abc import ABC, abstractmethod
from math import pi

###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively
#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.
#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']

class Patient:
    """
    A class to represent a patient in a hospital system.

    Attributes
    ----------
    name : str
        The name of the patient.
    symptoms : list of str
        The symptoms reported by the patient.
    tests : dict
        A dictionary to store test results for the patient.

    Methods
    -------
    add_test(self, test_name, test_result)
        Adds a test result to the patient's records.

    has_covid(self)
        Calculates the probability of the patient having COVID-19.

    """

    def __init__(self, name, symptoms):
        """
        Initializes a Patient object with the given name and symptoms.

        Parameters
        ----------
        name : str
            The name of the patient.
        symptoms : list of str
            The symptoms reported by the patient.
        """
        self.name = name
        self.symptoms = symptoms
        self.tests = {}

    def add_test(self, test_name, test_result):
        """
        Adds a test result to the patient's records.

        Parameters
        ----------
        test_name : str
            The name of the test.
        test_result : bool
            The result of the test.
        """
        self.tests[test_name] = test_result

    def has_covid(self):
        """
        Calculates the probability of the patient having COVID-19.

        Returns
        -------
        float
            The probability of the patient having COVID-19.
        """
        if 'covid' in self.tests:
            if self.tests['covid']:
                return 0.99
            else:
                return 0.01
        else:
            initial_prob = 0.05
            prob = sum(0.1 for symptom in self.symptoms if symptom.lower() in ['fever', 'cough', 'anosmia'])
            return min(1.0, initial_prob + prob)


######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    """
    A class to represent a playing card.

    Attributes
    ----------
    suit : str
        The suit of the card.
    value : str
        The value of the card.

    """

    def __init__(self, suit, value):
        """
        Initializes a Card object with the given suit and value.

        Parameters
        ----------
        suit : str
            The suit of the card.
        value : str
            The value of the card.
        """
        self.suit = suit
        self.value = value


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

class Deck:
    """
    A class to represent a deck of playing cards.

    Attributes
    ----------
    cards : list
        A list of Card objects representing the cards in the deck.

    Methods
    -------
    shuffle(self)
        Shuffles the deck of cards.

    draw(self)
        Draws a card from the deck and prints its suit and value.
    """

    def __init__(self):
        """
        Initializes a standard 52-card deck.
        """
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def draw(self):
        """
        Draws a card from the deck and prints its suit and value.

        If there are no more cards left in the deck, it prints a message indicating so.
        """
        if len(self.cards) > 0:
            card = self.cards.pop()
            print(f"Drawn Card: {card.value} of {card.suit}")
        else:
            print("No cards left in the deck.")


###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

# 3.1
class PlaneFigure(ABC):
    """
    An abstract class representing a plane figure.

    Methods
    -------
    compute_perimeter(self)
        Abstract method to compute the perimeter of the plane figure.

    compute_surface(self)
        Abstract method to compute the surface of the plane figure.
    """

    @abstractmethod
    def compute_perimeter(self):
        """
        Abstract method to compute the perimeter of the plane figure.
        """
        pass

    @abstractmethod
    def compute_surface(self):
        """
        Abstract method to compute the surface of the plane figure.
        """
        pass


# 3.2
class Triangle(PlaneFigure):
    """
    A class representing a triangle.

    Attributes
    ----------
    base : float
        The base of the triangle.
    c1 : float
        The first side of the triangle.
    c2 : float
        The second side of the triangle.
    h : float
        The height of the triangle.

    Methods
    -------
    compute_perimeter(self)
        Computes the perimeter of the triangle.

    compute_surface(self)
        Computes the surface of the triangle.
    """

    def __init__(self, base, c1, c2, h):
        """
        Initializes a Triangle object with the given parameters.

        Parameters
        ----------
        base : float
            The base of the triangle.
        c1 : float
            The first side of the triangle.
        c2 : float
            The second side of the triangle.
        h : float
            The height of the triangle.
        """
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        """
        Computes the perimeter of the triangle.

        Returns
        -------
        float
            The perimeter of the triangle.
        """
        return self.base + self.c1 + self.c2

    def compute_surface(self):
        """
        Computes the surface of the triangle.

        Returns
        -------
        float
            The surface of the triangle.
        """
        return 0.5 * self.base * self.h

# 3.3
class Rectangle(PlaneFigure):
    """
    A class representing a rectangle.

    Attributes
    ----------
    a : float
        The length of the rectangle.
    b : float
        The width of the rectangle.

    Methods
    -------
    compute_perimeter(self)
        Computes the perimeter of the rectangle.

    compute_surface(self)
        Computes the surface of the rectangle.
    """

    def __init__(self, a, b):
        """
        Initializes a Rectangle object with the given parameters.

        Parameters
        ----------
        a : float
            The length of the rectangle.
        b : float
            The width of the rectangle.
        """
        self.a = a
        self.b = b

    def compute_perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns
        -------
        float
            The perimeter of the rectangle.
        """
        return 2 * (self.a + self.b)

    def compute_surface(self):
        """
        Computes the surface of the rectangle.

        Returns
        -------
        float
            The surface of the rectangle.
        """
        return self.a * self.b


# 3.4
class Circle(PlaneFigure):
    """
    A class representing a circle.

    Attributes
    ----------
    radius : float
        The radius of the circle.

    Methods
    -------
    compute_perimeter(self)
        Computes the perimeter of the circle.

    compute_surface(self)
        Computes the surface of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle object with the given parameter.

        Parameters
        ----------
        radius : float
            The radius of the circle.
        """
        self.radius = radius

    def compute_perimeter(self):
        """
        Computes the perimeter of the circle.

        Returns
        -------
        float
            The perimeter of the circle.
        """
        return 2 * pi * self.radius

    def compute_surface(self):
        """
        Computes the surface of the circle.

        Returns
        -------
        float
            The surface of the circle.
        """
        return pi * (self.radius ** 2)
