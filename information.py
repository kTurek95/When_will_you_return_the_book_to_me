from database import Database
from datetime import datetime


class Information(Database):
    def __init__(self):
        super().__init__()

    def names_from_mail_list(self):
        char_to_find = '@'
        data = self.check_if_the_return_date_of_the_book_has_passed()
        names = []
        for mail_tuple in data:
            mail = mail_tuple[0]
            index_of_char = mail.find(char_to_find)
            names.append(mail[:index_of_char])

        return names

    def only_delay_dates(self, today=None):
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
        if today is None:
            today = datetime.today().date()
        delay = self.only_delay_dates(today)
        delay_days = []
        for date in delay:
            days_delay = today - date
            delay_days.append(days_delay.days)

        return delay_days