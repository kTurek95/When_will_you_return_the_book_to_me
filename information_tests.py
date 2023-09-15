"""
Module for testing the Information class methods.

This module includes a class `TestInformation` that inherits from `unittest.TestCase`.
It provides methods to test the functionality of the `Information` class.

Classes:
- TestInformation: A class for testing the `Information` class methods.

"""

import datetime
import unittest
from information import Information
from database_tests import create_database, remove_database


class TestInformation(unittest.TestCase):
    """
    A class for testing the Information class methods.

   This class inherits from unittest.TestCase and includes methods to test the
   functionality of the Information class.

   Methods:
   - setUp: Set up necessary resources before each test case.
   - test_names_from_mail_list: Test the names_from_mail_list method.
   - test_only_delay_days: Test the only_delay_days method.
   - test_empty_only_delay_days: Test the only_delay_days method with an empty result.
   - test_number_of_delay_days: Test the number_of_delay_days method.
   - test_empty_number_of_delay_days: Test the number_of_delay_days method with an empty result.

   Attributes:
   - library (Information): An instance of the Information class.

   """
    def setUp(self):
        """
        Set up necessary resources before each test case.
        """
        create_database()
        self.library = Information()
        self.library.create_connection('library.db')

    def test_names_from_mail_list(self):
        """

        This method tests the functionality of the names_from_mail_list method.
        It checks if the method returns the expected list of names.

        """
        remove_database()
        data = self.library.names_from_mail_list()
        expected_names = ['example', 'test', 'random']

        self.assertEqual(data, expected_names)
        self.assertCountEqual(data, expected_names)

    def test_only_delay_days(self):
        """

        This method tests the functionality of the only_delay_days method.
        It checks if the method returns the expected list of delay dates.

        """
        remove_database()
        today = datetime.date(2023, 8, 8)
        delay_dates = self.library.only_delay_dates(today)
        expected_dates = [datetime.date(2023, 8, 1),
                          datetime.date(2023, 8, 2),
                          datetime.date(2023, 8, 3)]

        self.assertEqual(delay_dates, expected_dates)
        self.assertCountEqual(delay_dates, expected_dates)

    def test_empty_only_delay_days(self):
        """

        This method tests the functionality of the only_delay_days method.
        It checks if the method returns the expected list of delay dates.

        """
        remove_database()
        today = datetime.date(2023, 7, 31)
        delay_dates = self.library.only_delay_dates(today)
        expected_dates = []

        self.assertEqual(delay_dates, expected_dates)
        self.assertCountEqual(delay_dates, expected_dates)

    def test_number_of_delay_days(self):
        """

        This method tests the functionality of the number_of_delay_days method.
        It checks if the method returns the expected list of delay days.

        """
        remove_database()
        today = datetime.date(2023, 8, 8)
        delay_days = self.library.number_of_delay_days(today)
        expected_days = [7, 6, 5]

        self.assertEqual(delay_days, expected_days)
        self.assertCountEqual(delay_days, expected_days)

    def test_empty_number_of_delay_days(self):
        """

       This method tests the functionality of the number_of_delay_days method when
       there are no delay days. It checks if the method returns an empty list.

       """
        remove_database()
        today = datetime.date(2023, 7, 31)
        delay_days = self.library.number_of_delay_days(today)
        expected_days = []

        self.assertEqual(delay_days, expected_days)
        self.assertCountEqual(delay_days, expected_days)


if __name__ == '__main__':
    unittest.main()
