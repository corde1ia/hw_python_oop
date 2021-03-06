## Калькулятор денег и калорий.
В проекте написана только логика - отдельный класс для каждого из калькуляторов.

#### Калькулятор денег умеет:
- Сохранять новую запись о расходах - метод add_record()
- Считать, сколько денег потрачено сегодня - метод get_today_stats()
- Считать, сколько денег потрачено за последние 7 дней — метод get_week_stats()
- Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод get_remained_balance()



#### Калькулятор калорий умеет:
- Сохранять новую запись о приёме пищи — метод add_record()
- Считать, сколько калорий уже съедено сегодня — метод get_today_stats()
- Определять, сколько ещё калорий можно/нужно получить сегодня — метод get_calories_remained()
- Считать, сколько калорий получено за последние 7 дней — метод get_week_stats()



#### Инструкция по установке
Клонируем репозиторий
```
git clone https://github.com/corde1ia/hw_python_oop.git
```

Переходим в папку с проектом
```
hw_python_oop/
```

Устанавливаем отдельное виртуальное окружение для проекта
```
python -m venv venv
```
Активируем виртуальное окружение
```
venv\Scripts\activate
```
Устанавливаем модули необходимые для работы проекта
```
pip install -r requirements.txt
```

#### Требования
Python 3.6 +
