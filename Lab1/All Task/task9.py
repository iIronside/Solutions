# Напишите программу, имитирующую работу банкомата. Выберите структуру
# данных для хранения купюр разного достоинства в заданном количестве.
# При вводе пользователем запрашиваемой суммы денег, скрипт должен вывести
# на консоль количество купюр подходящего достоинства. Если имеющихся денег
# не хватает, то необходимо напечатать сообщение «Операция не может быть
# выполнена!». Например, при сумме 5370 рублей на консоль должно быть
# выведено «5*1000 + 3*100 + 1*50 + 2*10».


def find_total_sum(moneydict={}):  # стиль именования аргументов в функции???
    balance = 0
    for price in moneydict:
        balance += price * moneydict[price]
    return balance


moneyAvailable = {10: 5, 50: 7, 100: 4, 500: 3, 1000: 4, 5000: 0}
requiredMoney = {}
availableSum = find_total_sum(moneyAvailable)

necessarySum = 5370  # int(input('How much money you need?\n'))
if availableSum >= necessarySum:
    tmp = 0
    for cost in sorted(moneyAvailable, reverse=True):  # reverse и reversed???
        tmp = necessarySum // cost
        if moneyAvailable[cost] > 0 and tmp <= moneyAvailable[cost]:
            requiredMoney[cost] = tmp
            necessarySum -= cost * tmp
        elif 0 < moneyAvailable[cost]:
            requiredMoney[cost] = moneyAvailable[cost]
            necessarySum -= cost * moneyAvailable[cost]
    for cost in sorted(requiredMoney, reverse=True):
        print("{}*{}".format(cost, requiredMoney[cost]))  # вывод с '+' ?
else:
    print('Операция не может быть выполнена!')

print(moneyAvailable)
print(requiredMoney)
