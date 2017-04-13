# Напишите скрипт, который читает текстовый файл и выводит символы в порядке
# убывания частоты встречаемости в тексте. Регистр символа не имеет значения.
# Программа должна учитывать только буквенные символы (символы пунктуации, цифры
# и служебные символы слудет игнорировать). Проверьте работу скрипта на нескольких
# файлах с текстом на английском и русском языках, сравните результаты с таблицами,
# приведенными в wikipedia.org/wiki/Letter_frequencies.


letterDict = {}
try:
    with open(r'E:\Мои документы\Питон\Lab2\text.txt', 'rt') as f:
        string = f.read()
        string.upper()
        for sym in string:
            if sym.isalpha():
                letterDict[sym] = letterDict.get(sym, 0) + 1
        print(sorted(letterDict.items(), key=lambda item: item[1]))
        print(letterDict)


except IOError as err:
    print(err)
