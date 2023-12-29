while True:
    number = int(input('Введите число: '))
    for i in range(number):
        if number > 0:
            print('Number is positive')
        elif number < 0:
            print('Number is negative')
        else:
            print('Number is equal to zero')
        if number == 7:
            print('Good Bye')
            break