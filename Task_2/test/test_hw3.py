#import sys
#sys.path.append("../")
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from datetime import date
import unittest
from hw3 import *


class TestCountSimba(unittest.TestCase):

    def test_count_simba_empty_list(self):
        empty_list = []
        output = count_simba(empty_list)
        expected_output = 0
        self.assertEqual(output,expected_output)

    def test_count_simba_0(self):
        list_zero = ['Mufasa only real king', 'Scar is a *****']
        output = count_simba(list_zero)
        expected_output = 0
        self.assertEqual(output,expected_output)

    def test_count_simba_3(self):
        list_three = ['Simba lion king', 'Simba loves Simba']
        output = count_simba(list_three)
        expected_output = 3
        self.assertEqual(output, expected_output)


class TestGetDayMonthYear(unittest.TestCase):
    def test_get_day_month_year(self):
        date_list = [date(2023, 10, 1), date(2023, 10, 2), date(2023, 10, 3)]
        expected_output = pd.DataFrame({'day': [1, 2, 3], 'month': [10, 10, 10], 'year': [2023, 2023, 2023]})
        output = get_day_month_year(date_list)
        assert_frame_equal(output, expected_output)

    def test_get_day_month_year_empty_list(self):
        date_list = []
        expected_output = pd.DataFrame({'day': [], 'month': [], 'year': []})
        output = get_day_month_year(date_list)
        pd.testing.assert_frame_equal(output, expected_output)


class TestComputeDistance(unittest.TestCase):
    def test_compute_distance(self):
        distance_list = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
        expected_output = [31.131865222052042, 157.005827868894]
        output = compute_distance(distance_list)
        self.assertEqual(output, expected_output)

    def test_compute_distance_empty_list(self):
        distance_list = []
        expected_output = []
        output = compute_distance(distance_list)
        self.assertEqual(output, expected_output)


class TestGeneralSum(unittest.TestCase):

    def test_general_sum_nly_integers(self):
        num_list = [1, 2, 3, 4, 5]
        expected_output = 15
        output = sum_general_int_list(num_list)
        self.assertEqual(output, expected_output)

    def test_general_sum_mixed_elements(self):
        num_list = [[2], 1, 2, [1, [2], [3, 5, [7,8]], 10], 1]
        expected_output = 42
        output = sum_general_int_list(num_list)
        self.assertEqual(output, expected_output)

    def test_general_sum_empty_list(self):
        num_list = []
        expected_output = 0
        output = sum_general_int_list(num_list)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
