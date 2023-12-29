numbers = [] #Список для хранения чисел

while True:
    number = int(input('Введите число: '))
    if number == 7:
        print('Good Bye!')
        break
    else:
        number.append(numbers) #Добавляем число в список

if numbers:
    print(f'Сумма веденных чисел: {sum(numbers)}')
    print(f'Максимальное число: {max(numbers)}')
    print(f'Минимальное число: {min(numbers)}')
else:
    print('Вы не ввели ни одного числа!')