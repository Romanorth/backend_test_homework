import datetime as dt

date_format = '%d.%m.%Y'
today = dt.datetime.now().date()

class Record:
    def __init__(self, amount, commit, date=None):
        self.amount = amount
        self.commit = commit

        if date is None:
            self.date = today

        elif date is not None:
            try:
                self.date = dt.datetime.strptime(date, date_format).date()

            except ValueError as val_err:
                print(
                      'Incorrect date format (correct:DDDD.MMMM.YYYY):',
                      val_err
                      )

            except TypeError as ty_err:
                print(
                      'Incorrect argument type (correct:string,'
                      ' example: "01.01.1999")', ty_err
                      )

    def __repr__(self):
        return f'{self.amount} {self.commit} {self.date}'

class Calculator:
    records = []

    def __init__(self, limit):
        self.limit = limit

    def add_record(self, record):
        self.records.append(record)

    def get_total_today(self):
        return self.get_total_per_day()

    def get_week_stats(self):
        pool = [0, 1, 2, 3, 4, 5, 6]
        now = dt.date.today()
        total_week_sum = 0

        for count in pool:
            day = now - dt.timedelta(days=count)
            print(day.strftime('%d.%m.%Y'))
            total_week_sum += self.get_total_per_day(day)
        return total_week_sum

    def get_total_per_day(self, date = None):
        total_sum = 0

        if date is None:
            self.date = today
            for row in self.records:
                if row.date == self.date:
                    total_sum += int(row.amount)

        elif date is not None:
            self.date = date
            for row in self.records:
                if row.date == self.date:
                    total_sum += int(row.amount)
        return total_sum

class CashCalculator(Calculator):
    currency_type = {
        'rub':'руб',
        'usd':'USD',
        'eur':'Euro'
                     }

    USD_RATE = 70.00
    EUR_RATE = 71.00

    def get_converted(self, total_today, currency):
        if currency == 'rub':
            total_limit = self.limit - total_today

        elif currency == 'usd':
            total_limit = (self.limit - total_today)/self.USD_RATE

        elif currency == 'eur':
            total_limit = (self.limit - total_today)/self.EUR_RATE

        return total_limit

    def get_today_cash_remainded(self, currency=None):
        if currency is None:
            currency = 'rub'

        total_today = self.get_total_per_day()

        if total_today < self.limit:
            result = self.get_converted(total_today, currency)
            return (
                'На сегодня осталось '
                f'{result:.2f} '
                f'{self.currency_type[currency]}'
                    )

        elif total_today == self.limit:
            return ('Денег нет, держись')

        elif total_today > self.limit:
            result = self.get_converted(total_today, currency)
            return (
            'Денег нет, держись:'
            f'твой долг - {result:.2f} '
            f'{self.currency_type[currency]}'
                   )

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        total_today = self.get_total_per_day()

        if total_today < self.limit:
            result = self.limit - total_today
            return ('Сегодня можно съесть что-нибудь ещё,'
            f' но с общей калорийностью не более {result:.2f} кКал')

        elif total_today >= self.limit:
            return 'Хватит есть!'

calc_1 = CashCalculator(100)
calc_1.add_record(Record(10,'text', '05.06.2020'))
calc_1.add_record(Record(10,'text', '06.06.2020'))
calc_1.add_record(Record(10,'text', '06.06.2020'))
calc_1.add_record(Record(10,'text'))
calc_1.add_record(Record(10,'text'))
calc_1.add_record(Record(10,'text'))
calc_1.add_record(Record(10,'text'))
calc_1.add_record(Record(10,'text'))
calc_1.add_record(Record(10,'text'))
calc_1.add_record(Record(11,'text'))
calc_1.add_record(Record(10,'text', '04.06.2020'))
calc_1.add_record(Record(10,'text', '05.06.2020'))
calc_1.add_record(Record(11,'text', '04.06.2020'))
calc_1.add_record(Record(10,'text', '03.06.2020'))
calc_1.add_record(Record(10,'text', '02.06.2020'))
calc_1.add_record(Record(10,'text', '01.06.2020'))
calc_1.add_record(Record(11,'text', '31.05.2020'))
calc_1.add_record(Record(10,'text', '30.05.2020'))
for i in calc_1.records:
    print(i)
print(calc_1.get_total_today())
print(calc_1.get_week_stats())
print(calc_1.get_today_cash_remainded())
print(calc_1.get_today_cash_remainded('usd'))
print(calc_1.get_today_cash_remainded('eur'))
calc_1.add_record(Record(9,'text', '06.06.2020'))
print(calc_1.get_today_cash_remainded())
calc_1.add_record(Record(19,'text', '06.06.2020'))
print(calc_1.get_today_cash_remainded())
print(calc_1.get_today_cash_remainded('usd'))
print(calc_1.get_today_cash_remainded('eur'))
calc_2 = CaloriesCalculator(1000)
print(calc_2.get_calories_remained())
calc_2.add_record(Record(881, 'text'))
print(calc_2.get_calories_remained())
