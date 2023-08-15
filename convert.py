from datetime import datetime


class Convert:
    @staticmethod
    def convert_to_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d').date()
