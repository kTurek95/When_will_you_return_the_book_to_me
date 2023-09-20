"""Module with Convert class"""
from datetime import datetime


class Convert:
    """
    A utility class for converting date strings to datetime.date objects.
    """
    @staticmethod
    def convert_to_date(date_str):
        """
       Convert a date string to a datetime.date object.

       Args:
           date_str (str): A date string in the format 'YYYY-MM-DD'.

       Returns:
           datetime.date: A datetime.date object representing the converted date.
        """
        return datetime.strptime(date_str, '%Y-%m-%d').date()
