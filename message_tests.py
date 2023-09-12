import unittest
from unittest.mock import patch
from datetime import datetime
import datetime
from message import Message
from database_tests import create_database, remove_database


class TestMessage(unittest.TestCase):
    def setUp(self):
        create_database()
        self.message = Message()
        self.message.create_connection('library.db')

    def test_message_format(self):
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
        today = datetime.date(2023, 7, 31)
        remove_database()
        user_message = self.message.message_format(today)
        expected_message = []

        self.assertEqual(user_message, expected_message)

    @patch('smtplib.SMTP_SSL')
    def test_send_mail(self, mock_smtp):
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