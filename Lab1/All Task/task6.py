# Напишите программу, позволяющую ввести с клавиатуры текст
# предложения и вывести на консоль все символы, которые входят
# в этот текст ровно по одному разу.

letterDict = {}
# string = str(input("Enter the string:\n"))
string = 'Напишите программу, позволяющую ввести с клавиатуры' \
         ' текст предложения и вывести на консоль все символы'
for i in range(len(string)):  # i или лучше именовать???
    if string[i] in letterDict:
        letterDict[string[i]] += 1
    else:
        letterDict[string[i]] = 1
for key in letterDict:
    if letterDict[key] < 2:
        print("{} -> {}".format(key, letterDict[key]))
