# 1.
# Импортируем тип date из модуля datetime.
from datetime import date

# Выводим текущую дату.
print(date.today())

# 2.
# Создаем объект, соответсвующий дате урагана.
hurricane_andrew = date(1992, 8, 24)

# Выводим день недели.
print(hurricane_andrew.weekday())
