"""
Module: message

This module provides a class, Message, that inherits from the Information class.
 The Message class is responsible for
formatting and sending email notifications to users with overdue book returns.

Classes:
- Message: Inherits from Information and contains methods to format and send email notifications.
"""
import smtplib
from os import getenv
from string import Template
from datetime import datetime
from dotenv import load_dotenv
from information.information import Information

load_dotenv()


class Message(Information):
    """
    Methods:
    - message_format(today=None):
     Formats a message to inform users about their overdue book returns.
    - smtp_settings(): Retrieves SMTP server settings from environment variables.
    - send_mail(): Sends email messages to users with delayed book returns.
    """
    def message_format(self, today=None):
        """
        Formats a message to inform users about their overdue book returns.

        Args:
        today (datetime.date, optional): The current date. Defaults to None.

        Returns:
        list: List of formatted messages for users.
        """
        if today is None:
            today = datetime.today().date()
        message = Template('Hello $first_name. '
                           'The deadline for returning the book has already passed.'
                           ' Could you please return it as soon as possible,'
                           ' as the due date was set for $date. You are $count days overdue.')

        names = self.names_from_mail_list()
        delay_days = self.number_of_delay_days(today)
        date_objects = self.only_delay_dates(today)
        user_message = []

        for name, return_date, delay_day in zip(names, date_objects, delay_days):
            text = message.substitute(first_name=name.upper(), date=return_date, count=delay_day)
            user_message.append(text)

        return user_message

    @staticmethod
    def smtp_settings():
        """
        Retrieves SMTP server settings from environment variables.

        Returns:
        tuple: A tuple containing SMTP server settings:
         (smtp_server, smtp_port, smtp_username, smtp_password, sender).
        """
        smtp_server = getenv('SMTP_SERVER')
        smtp_port = int(getenv('SMTP_PORT'))
        smtp_username = getenv('USERNAME')
        smtp_password = getenv('PASSWORD')
        sender = getenv('SENDER')

        return smtp_server, smtp_port, smtp_username, smtp_password, sender

    def send_mail(self):
        """
        Sends email messages to users with delayed book returns.

        Args:
        None.

        Returns:
        bool: True if the messages were sent successfully.
        """
        mails = self.check_if_the_return_date_of_the_book_has_passed()
        messages = self.message_format()
        smtp_server, smtp_port, smtp_username, smtp_password, sender = self.smtp_settings()

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            for user_mail, message in zip(mails, messages):
                if user_mail[0].startswith(message.split()[1].lower().rstrip('.')):
                    server.sendmail(sender, user_mail, message)
                    print(f'The email has been sent to {user_mail[0]}')
            return True
