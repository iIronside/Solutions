# Напишите скрипт, который на основе списка из 16 названий футбольных команд
# случайным образом формирует 4 группы по 4 команды, а также выводит на консоль
# календарь всех игр (игры должны проходить по средам, раз в 2 недели, начиная с
# 14 сентября текущего года). Даты игр необходимо выводить в формате
# «14/09/2016, 22:45». Используйте модули random и itertools.

import random
import itertools
import datetime


teams = ['Arsenal', 'Livepool', 'Manchester United', 'Barcelona',
         'Uventus', 'CSKA', 'Milan', 'Tottenham', 'Zenit',
         'Rubin', 'Lazio', 'Shakhtar', 'Chelsea', 'Celta',
         'No wooman', 'No cry']
groupSize = 4
groupList = []
gameDate = datetime.datetime(2017, 9, 20, 22, 45)
twoWeek = datetime.timedelta(days=14)

random.shuffle(teams)
print(teams)

start = 0
end = groupSize
while start < len(teams):
    groupList.append(teams[start:end])
    start += groupSize
    end += groupSize

print(groupList)

for group in groupList:
    games = list(itertools.combinations(group, 2))
    for game in games:
        print('{} {}'.format(gameDate, game))
        gameDate += twoWeek
