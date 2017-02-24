# Напишите скрипт, позволяющий определить надежность вводимого
# пользователем пароля. Это задание является творческим: алгоритм
# определения надежности разработайте самостоятельно.

securityScore = 0
specialSymbol = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '_', '~']
passwordParam = {'num': False, 'letter': False, 'letterUpCase': False}

password = 'M452m096'  # str(input('Enter the password:\n'))

if len(password) >= 10:
    securityScore += 4

for i in password:
    if i.isdigit() is True:
        passwordParam['num'] = True

    if i.isalpha() is True:
        passwordParam['letter'] = True
        if i.istitle():
            passwordParam['letterUpCase'] = True

for i in passwordParam:
    if passwordParam[i]:
        securityScore += 4

if securityScore > 12:
    print('Good password!')
elif 8 < securityScore <= 12:
    print('Normal password.')
else:
    print('It is a bad password!')
