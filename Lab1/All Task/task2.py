# Написать скрипт, который выводит на экран «True», если элементы
# программно задаваемого списка представляют собой возрастающую
# последовательность, иначе – «False».!!!

import random


def check(check_list=[]):  # стиль именования аргументов в функции???
    count = len(check_list) - 1
    n = 0
    while n < count:
        if check_list[n] > check_list[n+1]:
            return False
        n += 1
    return True

sequenceList = []
size = 100
i = 0
while i < size:
    i += 1
    sequenceList.append(i)
print(len(sequenceList))
print(check(sequenceList))
list2 = []
i = 0
while i < size:
    i += 1
    list2.append(random.randint(1, 1000))
print(check(list2))
print(list2)
