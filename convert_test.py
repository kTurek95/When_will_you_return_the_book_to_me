import datetime
from convert import Convert


def test_convert_to_date():
    date_str = '2020-02-02'

    assert Convert.convert_to_date(date_str) == datetime.date(2020, 2, 2)
    assert Convert.convert_to_date(date_str) != date_str
    assert type(Convert.convert_to_date(date_str)) == datetime.date
