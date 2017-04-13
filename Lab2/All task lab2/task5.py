# Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все слова,
# которые начинаются с большого латинского символа (от A до Z) и заканчиваются 2 или
# 4 цифрами, например «Petr93», «Johnny70», «Service2002». Используйте регулярные выражения.

import re


# string = str(input("Enter the path to the directory:\n"))
string = "hghbjgbhj Petr93, Johnny70 Service2002. jhjh duuu chbiisjd kkkk"
result = re.findall(r'[A-Z][a-z]*\d{2}\b', string)  # задать интервал?
print(result)
result = re.findall(r'[A-Z][a-z]*\d{4}\b', string)  # задать интервал?
print(result)
