# Напишите скрипт, который преобразует введенное с клавиатуры вещественное
# число в денежный формат. Например, число 12,5 должно быть преобразовано
# к виду «12 руб. 50 коп.». В случае ввода отрицательного числа выдайте
# сообщение «Некорректный формат!» путем обработки исключения в коде.

number = input('Enter the number:\n')
if number.isalpha() is False:
    number = float(number)
    fractionalPart = 0
    try:
        if number > 0:
            fractionalPart = number - int(number)
            fractionalPart *= 100
            print("{} руб. {} коп.".format(int(number), int(fractionalPart)))
        else:
            raise ValueError
    except ValueError:
        print('Incorrect format!')
else:
    print('It is not a number!')
