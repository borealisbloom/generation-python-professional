# 1.
# Тимур, Артур и новый курс.
def minimal_distance(d1, d2, d3):
    # Четыре возможных маршрута.
    route1 = d1 + d3 + d2  # Через оба магазина и соединяющую дорожку.
    route2 = 2 * (d1 + d3)  # Через первый магазин и возвращение через второй.
    route3 = 2 * (d2 + d3)  # Через второй магазин и возвращение через первый.
    route4 = 2 * d1 + 2 * d2  # Посещение обоих магазинов с возвращением домой каждый раз.

    # Минимальное расстояние.
    return min(route1, route2, route3, route4)

# Ввод данных.
d1 = int(input())
d2 = int(input())
d3 = int(input())

# Вывод минимального расстояния.
print(minimal_distance(d1, d2, d3))

# 2.
# Схожие буквы.
def same_letters(letters):
    d = {
        'en': 'abcehkmoptxy',
        'ru': 'авекмнорстух'
    }

    en = 0
    ru = 0

    for letter in letters:
        if letter.lower() in d['en']:
            en += 1
        elif letter.lower() in d['ru']:
            ru +=1

    if en == 3:
        return 'en'
    elif ru == 3:
        return 'ru'
    elif (0 < en < 3) and (0 < ru < 3):
        return 'mix'

letter1 = input()
letter2 = input()
letter3 = input()

print(same_letters([letter1, letter2, letter3]))

# 3.
# Переворатор.
def reverse(sequence):
    n, x, y, a, b = sequence

    numbers = list(range(1, n + 1))

    # Переворачиваем часть от X до Y.
    numbers[x - 1:y] = reversed(numbers[x - 1:y])

    # Переворачиваем часть от A до B.
    numbers[a - 1:b] = reversed(numbers[a - 1:b])

    numbers = [str(i) for i in numbers]
    return ' '.join(numbers)

sequence = [int(i) for i in input().split()]

print(reverse(sequence))

# 4.
# Более одного.
def more_than_one(sequence):
    result = []

    for i in sequence:
        if sequence.count(i) > 1 and i not in result:
            result.append(i)

    result = sorted([int(i) for i in result])

    return ' '.join([str(i) for i in result])

sequence = input().split()

print(more_than_one(sequence))

# 5.
# Максимальная группа.
def max_group_length(n):
    groups = {}

    def sum_of_digits(num):
        digit_sum = sum(int(digit) for digit in str(num))
        return digit_sum

    for num in range(1, n + 1):
        digit_sum = sum_of_digits(num)

        if digit_sum not in groups:
            groups[digit_sum] = []

        groups[digit_sum].append(num)

    max_lenght = max([len(group) for group in groups.values()])

    return max_lenght

n = int(input())
result = max_group_length(n)

print(result)

# 6.
# Трудности перевода.
def languages_intersection(languages):
    result = languages[0]

    for i in languages:
        result = result.intersection(i)

    if result:
        return ', '.join(sorted(list(result)))
    else:
        return f'Сериал снять не удастся'

n = int(input())
languages = [set(input().split(', ')) for _ in range(n)]

print(languages_intersection(languages))

# 7.
# Схожие слова.
def find_similar_words(base_word, words):
    vowels = 'ауоыиэяюёе'

    # Функция для извлечения индексов гласных.
    def extract_vowel_positions(word):
        return [i for i, char in enumerate(word) if char in vowels]

    # Позиции гласных для исходного слова.
    base_positions = extract_vowel_positions(base_word)

    # Фильтруем слова, у которых позиции гласных начинаются так же, как в базовом слове.
    similar_words = [word for word in words if extract_vowel_positions(word)[:len(base_positions)] == base_positions]

    if similar_words:
        return '\n'.join(similar_words)
    else:
        return f'Схожих слов нет'

base_word = input().strip().lower()
n = int(input())
words = [input().strip().lower() for _ in range(n)]

print(find_similar_words(base_word, words))

# 8.
# Корпоративная почта.
def assign_corporate_emails(existing_emails_list, new_users):
    # Преобразуем список существующих ящиков в множество для быстрого поиска.
    existing_emails = set(existing_emails_list)

    # Создаем словарь для подсчета количества выданных ящиков с одинаковыми именами.
    email_counts = {}
    result_emails = []

    # Обрабатываем новых сотрудников.
    for user in new_users:
        base_email = f"{user}@beegeek.bzz"

        if base_email not in existing_emails:
            # Если базовый ящик свободен, выдаем его.
            result_emails.append(base_email)
            existing_emails.add(base_email)
            email_counts[user] = 0
        else:
            # Если базовый ящик занят, добавляем номер.
            count = email_counts.get(user, 0) + 1

            while f"{user}{count}@beegeek.bzz" in existing_emails:
                count += 1

            email_counts[user] = count
            new_email = f"{user}{count}@beegeek.bzz"

            result_emails.append(new_email)
            existing_emails.add(new_email)

    return result_emails

n = int(input())
existing_emails_list = [input().strip() for _ in range(n)]

m = int(input())
new_users = [input().strip() for _ in range(m)]

assigned_emails = assign_corporate_emails(existing_emails_list, new_users)
print("\n".join(assigned_emails))

# 9.
# Файлы в файле.
UNITS = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
}

def convert_bytes(num: int) -> str:
    step_unit = 1024
    for unit in UNITS.keys():
        if num < step_unit:
            return f'{round(num)} {unit}'
        num /= step_unit

with open('files.txt', encoding='utf-8') as f:
    files = [file.strip() for file in f.readlines()]

file_extensions = {}

for file in files:
    file_name, file_size, file_unit = file.split()
    index = file_name.rfind('.')
    key = file_name[index:]
    bytes_size = int(file_size) * UNITS[file_unit]
    file_extensions.setdefault(key, []).append((file_name, bytes_size))

for extension in sorted(file_extensions.keys()):
    size = 0
    for file_name, file_size in sorted(file_extensions[extension]):
        print(file_name)
        size += file_size

    print('-' * 10)
    print(f'Summary: {convert_bytes(size)}\n')
