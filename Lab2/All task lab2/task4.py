# Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла,
# найти в нем с помощью регулярных выражений все подстроки определенного вида,
# в соответствии с вариантом.

import re


# path = str(input("Enter the path to the directory:\n"))
path = "E:\\Мои документы\\Питон\\Lab2\\forTask3.txt"

try:
    with open("E:\\Мои документы\\Питон\\Lab2\\forTask3.txt", 'rt') as f:
        string = f.read()
        result = re.findall(r'\d{3}.\d{3}.\d.\d{2}', string)
        print(result)

except IOError as err:
    print(err)
