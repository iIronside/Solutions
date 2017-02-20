# Напишите скрипт, который позволяет ввести с клавиатуры текст предложения и сформировать новую строку
# на основе исходной, в которой все слова, начинающиеся с большой буквы, приведены к верхнему регистру.
# Слова могут разделяться запятыми или пробелами. Например, если пользователь введет строку
# «город Донецк, река Кальмиус», результирующая строка должна выглядеть так: «город ДОНЕЦК, река КАЛЬМИУС».

string = 'город Донецк, река Кальмиус'
strList = string.split(' ')
for i in range(len(strList)):
    if strList[i].istitle():
        strList[i] = strList[i].upper()
string = ' '.join(strList)
print(string)