number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

# Инициализируем счетчики
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0
multiple_of_9_sum = 0
multiple_of_9_count = 0

# Находим суммы и количество четных, нечетных и чисел, кратных 9
for number in range(min(number1, number2), max(number1, number2) + 1):
    if number % 2 == 0:
        even_sum += number
        even_count += 1
    else:
        odd_sum += number
        odd_count += 1
    if number % 9 == 0:
        multiple_of_9_sum += number
        multiple_of_9_count += 1

# Находим среднеарифметическое каждой группы
if even_count > 0:
    even_average = even_sum / even_count
else:
    even_average = 0
if odd_count > 0:
    odd_average = odd_sum / odd_count
else:
    odd_average = 0
if multiple_of_9_count > 0:
    multiple_of_9_average = multiple_of_9_sum / multiple_of_9_count
else:
    multiple_of_9_average = 0

# Выводим результаты
print(f"Сумма четных чисел: {even_sum}, среднеарифметическое: {even_average}")
print(f"Сумма нечетных чисел: {odd_sum}, среднеарифметическое: {odd_average}")
print(f"Сумма чисел, кратных 9: {multiple_of_9_sum}, среднеарифметическое: {multiple_of_9_average}")