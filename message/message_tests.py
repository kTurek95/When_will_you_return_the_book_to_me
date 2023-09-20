"""
Module containing unit tests for the Message class.

This module defines a set of unit tests using the unittest framework to verify the
correct functionality of the Message class in the 'message' module. It includes tests
for message formatting and email sending capabilities.

Classes:
    TestMessage: A class containing tests for the Message class.

"""

import unittest
from unittest.mock import patch
from datetime import datetime
import datetime
from message.message import Message
from database.database_tests import create_database, remove_database


class TestMessage(unittest.TestCase):
    """
    Class containing tests for the Message class.

    Methods:
    setUp: Set up the environment before each test.
    tearDown: Clean up the environment after each test.
    test_message_format: Test the correctness of message formatting.
    test_empty_message_format: Test formatting of an empty message.
    test_send_mail: Test sending an email message.
    """

    def setUp(self):
        """
        Set up the environment before each test.
        """
        create_database()
        self.message = Message()
        self.message.create_connection('library.db')

    def test_message_format(self):
        """
        Test the correctness of message formatting.

        This function tests the message formatting process
         for different users with varying due dates.
        It sets a specific date and checks if the formatted messages match the expected messages.

        """
        today = datetime.date(2023, 8, 8)
        remove_database()
        user_message = self.message.message_format(today)
        expected_message = ['Hello EXAMPLE. '
                            'The deadline for returning the book has already passed.'
                            ' Could you please return it as soon as possible,'
                            ' as the due date was set for 2023-08-01. You are 7 days overdue.',
                            'Hello TEST. '
                            'The deadline for returning the book has already passed.'
                            ' Could you please return it as soon as possible,'
                            ' as the due date was set for 2023-08-02. You are 6 days overdue.',
                            'Hello RANDOM. '
                            'The deadline for returning the book has already passed.'
                            ' Could you please return it as soon as possible,'
                            ' as the due date was set for 2023-08-03. You are 5 days overdue.'
                            ]

        self.assertEqual(user_message, expected_message)

    def test_empty_message_format(self):
        """
        Test formatting of an empty message.

        This function tests the message formatting process when there is no message content.
        It sets a specific date and checks if the formatted message matches the expected empty list.

        """
        today = datetime.date(2023, 7, 31)
        remove_database()
        user_message = self.message.message_format(today)
        expected_message = []

        self.assertEqual(user_message, expected_message)

    @patch('smtplib.SMTP_SSL')
    def test_send_mail(self, mock_smtp):
        """
        Test sending an email message.

        This function tests the process of sending an email message using the Message class.
        It simulates a scenario where a message is sent to notify
         a user about an overdue book return.

        Args:
            mock_smtp (MagicMock): A MagicMock object for mocking the SMTP_SSL class.

        """
        expected_return_date = datetime.date(2023, 8, 3)
        today = datetime.date.today()
        days_number = (today - expected_return_date).days
        remove_database()

        instance = mock_smtp.return_value.__enter__.return_value
        instance.sendmail.return_value = {}

        create_database()
        sender = Message()
        sender.create_connection('library.db')
        sender.send_mail()

        remove_database()

        mock_smtp.assert_called()
        instance.login.assert_called()
        instance.sendmail.assert_called_with(
            'kacperinhoturinho@gmail.com',
            ('random@email.com',),
            'Hello RANDOM. '
            'The deadline for returning the book has already passed.'
            ' Could you please return it as soon as possible,'
            f' as the due date was set for 2023-08-03. You are {days_number} days overdue.'
            )


if __name__ == '__main__':
    unittest.main()
