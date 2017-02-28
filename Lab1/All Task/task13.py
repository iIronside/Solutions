# Напишите собственную версию генератора enumerate под названием extra_enumerate.
# В переменной cum хранится накопленная сумма на момент текущей итерации, в переменной
# frac – доля накопленной суммы от общей суммы на момент текущей итерации.
# Пример вывода: (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)


def extra_enumerate(sequence, start=0):
    total_sum = sum(sequence)
    cum = 0

    for elem in sequence:
        cum += elem
        frac = cum / total_sum
        yield elem, cum, frac

sequence = [1, 3, 4, 2]

for elem, cum, frac in extra_enumerate(sequence):
    print("({}, {}, {})".format(elem, cum, frac), end="")
