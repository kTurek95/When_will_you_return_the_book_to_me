"""
Module for handling information related to returns and delays.

This module contains a class `Information` that inherits from the `Database` class.
It provides methods to extract names from email addresses, find dates that have
passed the return date, and calculate the number of delay days for each return.

Classes:
- Information: A class for handling information related to returns and delays.

"""

from datetime import datetime
from database import Database


class Information(Database):
    """
    This class inherits from the Database class.

    Methods:
    - names_from_mail_list: Extracts names from email addresses.
    - only_delay_dates: Finds dates that have passed the return date.
    - number_of_delay_days: Calculates the number of delay days for each return.

    Attributes:
    - None
    """
    def __init__(self):
        super().__init__()

    def names_from_mail_list(self):
        """
        Extract names from email addresses.

        This method extracts names from email addresses stored in the database.

        Returns:
            list: A list of names.

        """
        char_to_find = '@'
        data = self.check_if_the_return_date_of_the_book_has_passed()
        names = []
        for mail_tuple in data:
            mail = mail_tuple[0]
            index_of_char = mail.find(char_to_find)
            names.append(mail[:index_of_char])

        return names

    def only_delay_dates(self, today=None):
        """
        Find dates that have passed the return date.

        Args:
            today (datetime.date, optional): The current date. Defaults to None.

        Returns:
            list: A list of dates that have passed.

        """
        if today is None:
            today = datetime.today().date()
        dates = self.when_was_return_date()
        delay_dates = []
        for date in dates:
            if date < today:
                date_obj = datetime.strptime(date.strftime('%Y-%m-%d'), '%Y-%m-%d').date()
                delay_dates.append(date_obj)

        return delay_dates

    def number_of_delay_days(self, today=None):
        """
        Calculate the number of delay days for each return.

        Args:
            today (datetime.date, optional): The current date. Defaults to None.

        Returns:
            list: A list of delay days for each return.

        """
        if today is None:
            today = datetime.today().date()
        delay = self.only_delay_dates(today)
        delay_days = []
        for date in delay:
            days_delay = today - date
            delay_days.append(days_delay.days)

        return delay_days
