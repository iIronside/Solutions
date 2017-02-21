#Напишите программу, имитирующую работу банкомата. Выберите структуру данных для хранения купюр разного достоинства в
# заданном количестве. При вводе пользователем запрашиваемой суммы денег, скрипт должен вывести на консоль
# количество купюр подходящего достоинства. Если имеющихся денег не хватает, то необходимо напечатать сообщение
# «Операция не может быть выполнена!».
# Например, при сумме 5370 рублей на консоль должно быть выведено «5*1000 + 3*100 + 1*50 + 2*10».

def findTotalSum(dict = {}):
    balance = 0
    for cost in dict:
        balance += cost * dict[cost]
    return balance


moneyAvailable = {10: 5, 50: 7, 100: 4, 500: 3, 1000: 4, 5000: 1}
requiredMoney = {}
availableSum = findTotalSum(moneyAvailable)

necessarySum = 5370#int(input('How much money you need?\n'))
if availableSum >= necessarySum:
    tmp = 0
    for cost in sorted(moneyAvailable, reverse=True):#reverse и reversed???????
        tmp = necessarySum // cost
        if tmp <= moneyAvailable[cost]:
            requiredMoney[cost] = tmp
            necessarySum -= cost * tmp
        else:
            requiredMoney[cost] = moneyAvailable[cost]
            necessarySum -= cost * moneyAvailable[cost]
else:
    print('Операция не может быть выполнена!')

print(moneyAvailable)
print(requiredMoney)