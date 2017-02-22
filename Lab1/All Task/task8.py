# Напишите скрипт, генерирующий случайным образом число n в
# диапазоне от 1 до 10000. Скрипт должен создать массив из
# n целых чисел, также сгенерированных случайным образом, и
# дополнить массив нулями до размера, равного ближайшей сверху
# степени двойки. Например, если в массиве было n=100 элементов,
# то массив нужно дополнить 28 нулями, чтобы в итоге был массив
# из 28=128 элементов (ближайшая степень двойки к 100 – это число
# 128, к 35 – это 64 и т.д.).

import random
number = random.randint(0, 10000)
mass = []

i = 0
while i < number:
    mass.append(random.randint(0, 10000))
    i += 1

powerTwo = 2

while powerTwo < number:
    powerTwo *= 2
while len(mass) < powerTwo:
    mass.append(0)
print(number)
print(powerTwo)
print(len(mass))

for i in range(len(mass)):
    print(mass[i])
