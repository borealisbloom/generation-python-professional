# 1.
from datetime import date, time, datetime, timedelta

text = 'Уважаемый пациент, доктор готов принять Вас 15.07.2022 в 08:30'
pattern = 'Уважаемый пациент, доктор готов принять Вас %d.%m.%Y в %H:%M'

dt = datetime.strptime(text, pattern)

print(dt)

# 2
seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(seconds))
print(dt.timestamp())

# 3.
times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

before_noon_count = 0
after_noon_count = 0

for purchase_time in times_of_purchases:
    if purchase_time.time().hour < 12:
        before_noon_count += 1
    else:
        after_noon_count += 1

if before_noon_count > after_noon_count:
    print('До полудня')
else:
    print('После полудня')

# 4.
dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

result_list = []
for i in range(len(dates)):
    date_time_result = datetime.combine(dates[i], times[i])
    result_list.append(date_time_result)

result_list = sorted(result_list, key=lambda dt: dt.second)

for result in result_list:
    print(result)

# 5.
data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

timestamps_dict = {}
for person, time_delta in data.items():
    timestamps_dict[person] = datetime.strptime(time_delta[1], '%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(time_delta[0], '%d.%m.%Y %H:%M:%S').timestamp()

timestamps_dict = dict(sorted(timestamps_dict.items(), key=lambda item: item[1]))

print(list(timestamps_dict.items())[0][0])

# 6.
# Читаем файл.
with open("diary.txt", encoding="utf-8") as file:
    data = file.read().strip()

# Разбиваем текст по пустым строкам, получая отдельные записи.
entries = data.split("\n\n")

# Парсим записи и извлекаем дату и время.
parsed_entries = []
for entry in entries:
    lines = entry.split("\n")
    date_time_str = lines[0].strip()  # Первая строка — дата и время.
    date_time_obj = datetime.strptime(date_time_str, "%d.%m.%Y; %H:%M")  # Преобразуем в datetime.
    parsed_entries.append((date_time_obj, entry.strip()))  # Сохраняем кортеж (дата, запись).

# Сортируем записи по дате и времени и сохраняем только текст записей.
sorted_entries = [entry for _, entry in sorted(parsed_entries, key=lambda x: x[0])]

print(*sorted_entries, sep='\n\n')

# 7.
def parse_dates(dates):
    """Функция преобразует список строковых дат в множество всех забронированных дат."""
    booked_days = set()

    for date in dates:
        if '-' in date:  # Если это период (две даты через дефис)
            start, end = date.split('-')
            start_date = datetime.strptime(start, "%d.%m.%Y")
            end_date = datetime.strptime(end, "%d.%m.%Y")

            # Добавляем все даты из диапазона в множество
            current_date = start_date
            while current_date <= end_date:
                booked_days.add(current_date)
                current_date += timedelta(days=1)
        else:  # Если это одиночная дата
            booked_days.add(datetime.strptime(date, "%d.%m.%Y"))

    return booked_days

def is_available_date(booked_dates, date_for_booking):
    """Проверяет, доступна ли указанная дата или период для бронирования."""
    booked_days = parse_dates(booked_dates)  # Преобразуем забронированные даты в множество.

    if '-' in date_for_booking:  # Если гость хочет забронировать период.
        start, end = date_for_booking.split('-')
        start_date = datetime.strptime(start, "%d.%m.%Y")
        end_date = datetime.strptime(end, "%d.%m.%Y")

        # Проверяем, пересекаются ли даты с уже забронированными.
        current_date = start_date
        while current_date <= end_date:
            if current_date in booked_days:
                return False
            current_date += timedelta(days=1)
    else:  # Если гость хочет забронировать одиночную дату.
        if datetime.strptime(date_for_booking, "%d.%m.%Y") in booked_days:
            return False

    return True
