# 1.
# Функция hide_card().
def hide_card(card_number):
    card_number = card_number.replace(' ', '')
    result = '*' * len(card_number[:-4]) + card_number[-4:]

    return result

print(hide_card('905 678123 45612 56'))

# 2.
# Функция same_parity().
# def same_parity(numbers):
#     if len(numbers) > 0:
#         first_num = numbers[0]
#
#         if first_num % 2 == 0:
#             is_even = True
#             is_odd = False
#         else:
#             is_even = False
#             is_odd = True
#
#         result = []
#         for i in numbers:
#             if (i % 2 == 0) and is_even:
#                 result.append(i)
#             elif (i % 2 != 0) and is_odd:
#                 result.append(i)
#
#         return result
#
#     else:
#         return numbers

def same_parity(numbers):
    if not numbers:
        return numbers

    parity = numbers[0] % 2  # Определяем четность первого числа.
    return [num for num in numbers if num % 2 == parity]

print(same_parity([-7, 0, 67, -9, 70, -29, 90]))

# 3.
# Функция is_valid().
# def is_valid(pin_code):
#     if (len(pin_code) > 3 and len(pin_code) < 7) and \
#         (pin_code.isdigit()):
#         return True
#     else:
#         return False

def is_valid(pin):
    return pin.isdigit() and len(pin) in (4, 5, 6)

print(is_valid('89abc1'))

# 4.
# Функция print_given().
def print_given(*args, **kwargs):
    for arg in args:
        print(f'{arg} {type(arg)}')

    for key in sorted(kwargs.keys()):
        print(f'{key} {kwargs[key]} {type(kwargs[key])}')

print_given(1, [1, 2, 3], 'three', two=2)

# 5.
# Функция convert().
import string
def convert(text):
    lower_case_symbols = len(list(filter(lambda x: x in string.ascii_lowercase, text)))
    upper_case_symbols = len(list(filter(lambda x: x in string.ascii_uppercase, text)))

    if lower_case_symbols >= upper_case_symbols:
        return text.lower()
    else:
        return text.upper()

print(convert('ABCdef'))

# 6.
# Функция filter_anagrams().
def filter_anagrams(word, words):
    word = sorted(word)
    result = []

    for i in words:
        if word == sorted(i):
            result.append(i)

    return result

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

# 7.
# Функция likes().
def likes(users):
    if users:
        if len(users) == 1:
            return f'{users[0]} оценил(а) данную запись'
        elif len(users) == 2:
            return f'{users[0]} и {users[1]} оценили данную запись'
        elif len(users) == 3:
            return f'{users[0]}, {users[1]} и {users[2]} оценили данную запись'
        elif len(users) > 3:
            return f'{users[0]}, {users[1]} и {len(users[2:])} других оценили данную запись'
    else:
        return f'Никто не оценил данную запись'

print(likes(['Артур', 'Тимур', 'Руслан', 'Анри', 'Дима', 'Алиса']))

# 8.
# Функция index_of_nearest().
def index_of_nearest(numbers, number):
    if numbers:
        diff = [abs(number - i) for i in numbers]
        index = diff.index(min(diff))
        return index
    else:
        return -1

print(index_of_nearest([7, 13, 3, 5, 18], 0))

# 9.
# Функция spell().
def spell(*args):
    words = args
    result = {}

    for word in words:
        first_letter = word[0].lower()
        word_lenght = len(word)

        if first_letter in result:
            result[first_letter] = max(result[first_letter], word_lenght)
        else:
            result[first_letter] = word_lenght

    return result

words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))

# 10.
# Функция choose_plural().
# Правило выбора склонения:
# - Если число в диапазоне от 11 до 19 включительно (например, 11, 12, 13), то всегда используется третья форма (примеров).
# - Если последняя цифра числа равна 1 (и число не в диапазоне от 11 до 19), используется первая форма (пример).
# - Если последняя цифра числа равна 2, 3 или 4 (и число не в диапазоне от 11 до 19), используется вторая форма (примера).
# - В остальных случаях — третья форма (примеров).
def choose_plural(amount, declensions):
    # Правило выбора склонения.
    if 11 <= amount % 100 <= 19:
        form = declensions[2]
    elif amount % 10 == 1:
        form = declensions[0]
    elif 2 <= amount % 10 <= 4:
        form = declensions[1]
    else:
        form = declensions[2]

    return f"{amount} {form}"

print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))

# 11.
# Функция get_biggest().
from functools import cmp_to_key
def get_biggest(numbers):
    # Если список пуст, возвращаем -1.
    if not numbers:
        return -1

    # Определяем функцию сравнения для сортировки.
    def compare(x, y):
        # Сравниваем комбинации x+y и y+x как строки.
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Преобразуем числа в строки и сортируем их.
    sorted_numbers = sorted(map(str, numbers), key=cmp_to_key(compare))

    # Собираем наибольшее число.
    biggest_number = ''.join(sorted_numbers)

    # Убираем ведущие нули (например, если numbers = [0, 0]).
    return int(biggest_number) if biggest_number else 0

print(get_biggest([61, 228, 9, 3, 11]))
