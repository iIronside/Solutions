# Напишите скрипт, который позволяет ввести с клавиатуры номер
# дебетовой карты (16 цифр) и выводит номер в скрытом виде:
# первые и последние 4 цифры отображены нормально,
# а между ними – символы «*» (например, 5123 **** **** 1212).

number = str(input("Enter the number:\n"))
if len(number) == 16:
    for num in range(len(number)):
        if num < 4 or num > 11:
            print(number[num], end='')
        else:
            print('*', end='')
else:
    print('Incorrect format!')
