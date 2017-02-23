# Напишите скрипт, который разделяет введенный с клавиатуры текст на слова
# и выводит сначала те слова, длина которых превосходит 7 символов,
# затем слова размером от 4 до 7 символов, затем – все остальные.


def sort_by_len(input_str):  # стиль именования аргументов в функции???
    return len(input_str)

enterWords = "Напишите скрипт, который разделяет введенный с клавиатуры" \
             " текст на слова и выводит сначала те слова, длина которых" \
             " превосходит 7 символов, затем слова размером от 4 до 7 4" \
             "символов, затем – все остальные."
words = ''
punctuation_marks = [',', '.', '(', ')', '"', '–', ':']
for i in range(len(enterWords)):
    if enterWords[i] in punctuation_marks:
        continue
    else:
        words += enterWords[i]
wordsList = words.split(' ')
wordsList.sort(key=sort_by_len, reverse=True)
print(wordsList)
