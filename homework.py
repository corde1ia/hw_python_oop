"""Код для создания калькулятора
днегег и калькулятора калорий."""

import datetime as dt
from typing import Optional


DATE_FORMAT = '%d.%m.%Y'


class Record:
    """Класс, содержащий в себе описание структуры данных
    для записей калькулятора калорий/денег."""
    amount: float
    comment: str
    date: Optional[str]

    def __init__(self, amount, comment, date=None) -> None:
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
        else:
            self.date = dt.date.today()


class Calculator:
    """Класс, содержащий общие методы для
    добавления новых записей и вычисления данных
    для калькулятора денег/калькулятора ккал."""
    limit: float

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, record: Record) -> list:
        """Метод, добавляющий новые записи для
        калькуляторов ккал/денег."""
        self.records.append(record)

    def get_today_stats(self) -> float:
        """"Метод для вывода данных о ккал/деньгах за день."""
        today_stats = 0
        date_today = dt.date.today()
        today_stats = sum(r.amount for r in self.records
                          if r.date == date_today)
        return today_stats

    def get_week_stats(self) -> float:
        """Метод для вывода данных о ккал/деньгах за неделю."""
        week_stats = 0
        today = dt.datetime.now().date()
        week_ago = today - dt.timedelta(weeks=1)
        week_stats = sum(r.amount for r in self.records
                         if today >= r.date > week_ago)
        return week_stats

    def get_remained_balance(self):
        """Метод для получения остатка калорий
        или денег."""
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """Дочерний класс Кальулятора - Калькулятор калорий."""
    def get_calories_remained(self) -> str:
        """Метод, вычисляющий остаток калорий,
        доступных для употребления."""
        remained_balance = self.get_remained_balance()
        if remained_balance > 0:
            return ("Сегодня можно съесть что-нибудь ещё, "
                    "но с общей калорийностью не более "
                    f"{remained_balance} кКал")
        return "Хватит есть!"


class CashCalculator(Calculator):
    "Дочерний класс Калькулятора - Калькулятор денег."
    USD_RATE: float = 60.00
    EURO_RATE: float = 70.00
    RUB_RATE: float = 1.00

    def get_today_cash_remained(self, currency) -> str:
        """Метод, вычисляющий остаток денежных средств,
        доступных для трат, в заданной валюте."""
        RATES = {
            "usd": (self.USD_RATE, "USD"),
            "eur": (self.EURO_RATE, "Euro"),
            "rub": (self.RUB_RATE, "руб")
        }

        if currency not in RATES:
            return "Неизвестная валюта"

        rate, currency_name = RATES[currency]
        remained_balance = self.get_remained_balance()
        cash_remained = round(remained_balance / rate, 2)

        if cash_remained > 0:
            return ("На сегодня осталось "
                    f"{cash_remained} {currency_name}")
        elif cash_remained == 0:
            return "Денег нет, держись"
        return ("Денег нет, держись: твой долг - "
                f"{abs(cash_remained)} {currency_name}")
