import datetime as dt

date_format = '%d.%m.%Y'
today = dt.datetime.now().date()

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

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
        return f'{self.amount} {self.comment} {self.date}'

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        return self.get_stats_per_day()

    def get_week_stats(self):
        pool = [0, 1, 2, 3, 4, 5, 6]
        now = dt.date.today()
        total_week_sum = 0

        for count in pool:
            day = now - dt.timedelta(days=count)
            total_week_sum += self.get_stats_per_day(day)
        return total_week_sum

    def get_stats_per_day(self, date = None):
        total_sum = 0

        if date is None:
            self.date = today
            for row in self.records:
                if row.date == self.date:
                    total_sum += row.amount

        elif date is not None:
            self.date = date
            for row in self.records:
                if row.date == self.date:
                    total_sum += row.amount
        return total_sum

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        total_today = self.get_stats_per_day()

        if total_today < self.limit:
            result = self.limit - total_today
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {result} кКал.'

        elif total_today >= self.limit:
            return 'Хватит есть!'

calc1 = CaloriesCalculator(100)
calc1.add_record(Record(50, 'text'))
calc1.add_record(Record(49, 'text'))
print(calc1.get_calories_remained())
calc1.add_record(Record(1,'text'))
print(calc1.get_calories_remained())
calc1.add_record(Record(1,'text'))
print(calc1.get_calories_remained())
