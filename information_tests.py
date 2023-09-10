import datetime
import unittest
from information import Information
from database_tests import create_database, remove_database


class TestInformation(unittest.TestCase):
    def setUp(self):
        create_database()
        self.library = Information()
        self.library.create_connection('library.db')

    def test_names_from_mail_list(self):
        remove_database()
        data = self.library.names_from_mail_list()
        expected_names = ['example', 'test', 'random']

        self.assertEqual(data, expected_names)
        self.assertCountEqual(data, expected_names)

    def test_only_delay_days(self):
        remove_database()
        today = datetime.date(2023, 8, 8)
        delay_dates = self.library.only_delay_dates(today)
        expected_dates = [datetime.date(2023, 8, 1),
                          datetime.date(2023, 8, 2),
                          datetime.date(2023, 8, 3)]

        self.assertEqual(delay_dates, expected_dates)
        self.assertCountEqual(delay_dates, expected_dates)

    def test_empty_only_delay_days(self):
        remove_database()
        today = datetime.date(2023, 7, 31)
        delay_dates = self.library.only_delay_dates(today)
        expected_dates = []

        self.assertEqual(delay_dates, expected_dates)
        self.assertCountEqual(delay_dates, expected_dates)

    def test_number_of_delay_days(self):
        remove_database()
        today = datetime.date(2023, 8, 8)
        delay_days = self.library.number_of_delay_days(today)
        expected_days = [7, 6, 5]

        self.assertEqual(delay_days, expected_days)
        self.assertCountEqual(delay_days, expected_days)

    def test_empty_number_of_delay_days(self):
        remove_database()
        today = datetime.date(2023, 7, 31)
        delay_days = self.library.number_of_delay_days(today)
        expected_days = []

        self.assertEqual(delay_days, expected_days)
        self.assertCountEqual(delay_days, expected_days)


if __name__ == '__main__':
    unittest.main()