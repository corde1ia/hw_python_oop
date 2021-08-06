import datetime as dt
from typing import Optional


class Record:
    """Класс, содержащий в себе описание структуры данных
    для записей калькуляторов калорий/денег."""
    amount: float
    comment: str
    date: Optional[str]

    def __init__(self, amount, comment, date=None) -> None:
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
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
        for r in self.records:
            if r.date == dt.date.today():
                today_stats += r.amount
        return today_stats

    def get_week_stats(self) -> float:
        """Метод для вывода данных о ккал/деньгах за неделю."""
        week_stats = 0
        week_ago = dt.datetime.now().date() - dt.timedelta(weeks=1)
        for r in self.records:
            if r.date > week_ago and r.date <= dt.datetime.now().date():
                week_stats += r.amount
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
        else:
            return ("Хватит есть!")


class CashCalculator(Calculator):
    "Дочерний класс Калькулятора - Калькулятор денег."
    USD_RATE: float = 60.00
    EURO_RATE: float = 70.00
    RUB_RATE: float = 1.00

    def get_today_cash_remained(self, currency) -> str:
        """Метод, вычисляющий остато денежных средств,
        доступных для траты, в заданной валюте."""
        RATES: dict
        RATES = {
            "usd": (self.USD_RATE, "USD"),
            "eur": (self.EURO_RATE, "Euro"),
            "rub": (self.RUB_RATE, "руб")
        }

        rate, currency_name = RATES[currency]
        today_stats = super().get_today_stats()
        cash_remained = round((self.limit - today_stats) / rate, 2)

        if currency not in RATES.keys():
            return ("Неизвестная валюта")
        else:
            if cash_remained > 0:
                return (f"На сегодня осталось {cash_remained} {currency_name}")
            elif cash_remained == 0:
                return ("Денег нет, держись")
            else:
                return (f"Денег нет, держись: твой долг - "
                        f"{abs(cash_remained)} {currency_name}")
