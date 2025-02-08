# 1.
# Импортируем тип date из модуля datetime.
from datetime import date, timedelta

# Выводим текущую дату.
print(date.today())

# 2.
# Создаем объект, соответсвующий дате урагана.
hurricane_andrew = date(1992, 8, 24)

# Выводим день недели.
print(hurricane_andrew.weekday())

# 3.
florida_hurricane_dates = []
early_hurricanes = 0

for hurricane in florida_hurricane_dates:
    if hurricane.month < 6:
        early_hurricanes += 1

print(early_hurricanes)

# 4.
dates = [date(2010, 9, 28),
         date(2017, 1, 13),
         date(2009, 12, 25),
         date(2010, 2, 27),
         date(2021, 10, 11),
         date(2020, 3, 13),
         date(2000, 7, 7),
         date(1999, 4, 14),
         date(1789, 11, 19),
         date(2013, 8, 21),
         date(1666, 6, 6),
         date(1968, 5, 26)]

month_to_quarter = {
    1: 1, 2: 1, 3: 1,
    4: 2, 5: 2, 6: 2,
    7: 3, 8: 3, 9: 3,
    10: 4, 11: 4, 12: 4
}
for one_date in dates:
    print(f"{one_date.year}-Q{month_to_quarter[one_date.month]}")

# 5.
def get_min_max(dates):
    if dates:
        return (min(dates), max(dates))
    else:
        return ()

dates = [date(2021, 10, 5),
         date(1992, 6, 10),
         date(2012, 2, 23),
         date(1995, 10, 12)]

print(get_min_max(dates))

# 6.
def get_date_range(start, end):
    if start > end:
        return []

    return [start + timedelta(days=i) for i in range((end - start).days + 1)]

def get_date_range(start, end):
    if start > end:
        return []

    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

# 7.
def saturdays_between_two_dates(date1, date2):
    start = min(date1, date2)
    end = max(date1, date2)

    count = 0
    dates = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

    for date_one in dates:
        if date_one.isoweekday() == 6:
            count += 1

    return count

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))
