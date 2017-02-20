#Напишите скрипт, который разделяет введенный с клавиатуры текст на слова и выводит сначала те слова,
#  длина которых превосходит 7 символов,
#  затем слова размером от 4 до 7 символов, затем – все остальные.
#enterWords = str(input("Enter the number:\n"))

def sortByLenght(inputStr):
    return len(inputStr)

words = "Напишите скрипт, который разделяет введенный с клавиатуры текст на слова и выводит сначала те слова, длина которых превосходит 7 символов, затем слова размером от 4 до 7 символов, затем – все остальные."
words2 = ''
for i in range(len(words)):
    if words[i] == ',' or words[i] == '.' or words[i] == '(' or words[i] == ')' or words[i] == '"' or words[i] == '–':
        continue
    else:
        words2 += words[i]
wordsList = words2.split(' ')
wordsList.sort(key=sortByLenght, reverse=True)
print(wordsList)