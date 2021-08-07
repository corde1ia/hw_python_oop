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
        """Метод, добавляющий новые записи для ккал/денег."""
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
        week_ago = dt.datetime.now().date() - dt.timedelta(weeks=1)
        week_stats = sum(r.amount for r in self.records
                         if dt.datetime.now().date() >= r.date > week_ago)
        return week_stats


class CaloriesCalculator(Calculator):
    """Дочерний класс Кальулятора - Калькулятор калорий."""
    def get_calories_remained(self) -> str:
        """Метод, вычисляющий остаток калорий,
        доступных для употребления."""
        remainded = self.limit - super().get_today_stats()
        if super().get_today_stats() < self.limit:
            return (f"Сегодня можно съесть что-нибудь ещё, "
                    f"но с общей калорийностью не более {remainded} кКал")
        return "Хватит есть!"


class CashCalculator(Calculator):
    "Дочерний класс Калькулятора - Калькулятор денег."
    USD_RATE: float = 60.00
    EURO_RATE: float = 70.00
    RUB_RATE: float = 1.00

    def get_today_cash_remained(self, currency) -> str:
        """Метод, вычисляющий остато денежных средств,
        доступных для траты, в заданной валюте."""
        RATES = {
            "usd": (self.USD_RATE, "USD"),
            "eur": (self.EURO_RATE, "Euro"),
            "rub": (self.RUB_RATE, "руб")
        }

        if currency not in RATES:
            return "Неизвестная валюта"

        rate, currency_name = RATES[currency]
        today_stats = super().get_today_stats()
        cash_remained = round((self.limit - today_stats) / rate, 2)

        if cash_remained > 0:
            return (f"На сегодня осталось {cash_remained} {currency_name}")
        elif cash_remained == 0:
            return ("Денег нет, держись")
        return (f"Денег нет, держись: твой долг - "
                f"{abs(cash_remained)} {currency_name}")
