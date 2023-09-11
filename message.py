import smtplib
from os import getenv
from string import Template
from dotenv import load_dotenv
from datetime import datetime
from information import Information

load_dotenv()


class Message(Information):
    def message_format(self, today=None):
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
        smtp_server = getenv('SMTP_SERVER')
        smtp_port = int(getenv('SMTP_PORT'))
        smtp_username = getenv('USERNAME')
        smtp_password = getenv('PASSWORD')
        sender = getenv('SENDER')

        return smtp_server, smtp_port, smtp_username, smtp_password, sender

    def send_mail(self):
        mails = self.check_if_the_return_date_of_the_book_has_passed()
        messages = self.message_format()
        smtp_server, smtp_port, smtp_username, smtp_password, sender = self.smtp_settings()

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            for user_mail, message in zip(mails, messages):
                if user_mail[0].startswith(message.split()[1].lower().rstrip('.')):
                    server.sendmail(sender, user_mail, message)
                    print(f'Udało się wysłać maila do {user_mail[0]}')
            return True
