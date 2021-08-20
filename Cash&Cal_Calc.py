import datetime as dt
today = dt.datetime.today().strftime("%d.%m.%Y")
class Record:
    def __init__(self, amount, comment, date=today):
        self.amount= amount
        self.comment= comment
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        


class Calculator:
    def __init__ (self, limit):
        self.limit= limit
        self.records= []
    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):        
        today = dt.date.today()
        return sum(record.amount for record in self.records 
                   if record.date == today)

    def get_week_stats(self):
        today = dt.date.today()       
        week = today - dt.timedelta(days= 7)                
        return sum(record.amount for record in self.records 
                   if week < record.date <= today)
    def get_today_remainder(self):
        return self.limit - self.get_today_stats()

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remainder = self.limit - self.get_today_stats()
        if calories_remainder > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей'
                    f' калорийностью не более {calories_remainder} кКал')
        else:
            return 'Хватит есть!'

class CashCalculator(Calculator):
    RUB_RATE = 1.0
    USD_RATE = 74.0
    EURO_RATE = 87.0
    currencies = {"rub": (RUB_RATE, "RUB"),
                  "usd": (USD_RATE, "USD"),
                  "eur": (EURO_RATE, "EURO")
                         }
    def get_today_cash_remained(self, currency):
        if currency not in self.currencies:
            return "Убирай свои фантики"
        cash_remainder= self.get_today_remainder()
        if cash_remainder == 0:
            return ("Умри в нищете")
        rate, name = self.currencies[currency]
        cash_remainder_= cash_remainder/rate
        if cash_remainder > 0:
            return(f'На сегодня осталось: {cash_remainder_} {name}')
        else:
            return(f'Денег нет, держись: твой долг составляет - {cash_remainder_} {name}')

cash_calculator = CashCalculator(445)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб 