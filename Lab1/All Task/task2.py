#Написать скрипт, который выводит на экран «True»,
#если элементы программно задаваемого списка представляют собой возрастающую последовательность,
#иначе – «False».!!!
import  random

def checkList(list, size):
    x = 0
    while x < size:
        print(list[x])

list1 = []
list2 = []
i = 0
while i < 10:
    i+=1
    print(i)#list1[i] = random.randrange(0,100)#error!!!
i = 0
while i < 10:
    i += 1
    list2[i] = i + 1
checkList(list2, len(list2))