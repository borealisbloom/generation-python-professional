# 1.
# Импортируем тип date из модуля datetime.
from datetime import time, date

alarm = time(7, 30, 25)

print('Часы:', alarm.strftime('%H'))
print('Минуты:', alarm.strftime('%M'))
print('Секунды:', alarm.strftime('%S'))

# 2.
birthday = date(1992, 10, 6)

print('Название месяца:', birthday.strftime('%B'))  # October.
print('Название дня недели:', birthday.strftime('%A'))  # Tuesday.
print('Год:', birthday.strftime('%Y'))  # 1992.
print('Месяц:', birthday.strftime('%m'))  # 10.
print('День:', birthday.strftime('%d'))  # 06.

# 3.
florida_hurricane_dates = []

# Присваиваем самую раннюю дату урагана в переменную first_date.
first_date = min(florida_hurricane_dates)

# Конвертируем дату в ISO и RU формат.
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d.%m.%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m/%d/%Y')

print(iso)
print(ru)
print(us)

# 4.
andrew = date(1992, 8, 24)

print(andrew.strftime('%Y-%m'))  # Формат YYYY-MM.
print(andrew.strftime('%B (%Y)'))  # Формат month_name (YYYY).
print(andrew.strftime('%Y-%j'))  # Формат YYYY-day_number.

# 5.
# Считываем две даты.
date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())

# Определяем меньшую дату.
min_date = min(date1, date2)

# Выводим результат в нужном формате.
print(min_date.strftime('%d-%m (%Y)'))

# 6.
# Считываем количество дат.
n = int(input().strip())

# Считываем даты и преобразуем их в объекты date.
dates = [date.fromisoformat(input()) for _ in range(n)]

# Сортируем даты в порядке неубывания.
dates.sort()

# Выводим отсортированные даты в нужном формате.
for d in dates:
    print(d.strftime('%d/%m/%Y'))

# 7.
def print_good_dates(dates):
    # Фильтруем "интересные" даты.
    good_dates = [d for d in dates if d.year == 1992 and (d.month + d.day) == 29]

    # Сортируем по возрастанию.
    good_dates.sort()

    # Выводим в нужном формате.
    for d in good_dates:
        print(d.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)

# 8.
def is_correct(day, month, year):
    try:
        # Пытаемся создать объект date с переданными значениями.
        date(year, month, day)
        return True
    except ValueError:
        # Если ошибка, то дата некорректна.
        return False

print(is_correct(31, 12, 2021))

# 9.
def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

# Инициализируем счетчик корректных дат.
correct_count = 0

while True:
    # Считываем ввод.
    user_input = input()

    # Проверяем условие окончания.
    if user_input.lower() == "end":
        break

    # Разбираем дату.
    try:
        day, month, year = map(int, user_input.split('.'))
        if is_correct(day, month, year):
            print("Корректная")
            correct_count += 1
        else:
            print("Некорректная")
    except ValueError:
        print("Некорректная")

# Выводим количество корректных дат.
print(correct_count)
