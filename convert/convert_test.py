"""Module with tests for Convert class"""
import datetime
from convert.convert import Convert


def test_convert_to_date():
    """
    Test function for the Convert.convert_to_date() method

    The function performs the following checks:
    1. The converted date should match the expected datetime.date(2020, 2, 2).
    2. The converted date should not be equal to the input date string.
    3. The type of the converted date should be datetime.date.

    """
    date_str = '2020-02-02'

    assert Convert.convert_to_date(date_str) == datetime.date(2020, 2, 2)
    assert Convert.convert_to_date(date_str) != date_str
    assert type(Convert.convert_to_date(date_str)) == datetime.date
