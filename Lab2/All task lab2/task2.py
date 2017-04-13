# Напишите скрипт, позволяющий искать в заданной директории и в ее подпапках
# файлы-дубликаты на основе сравнения контрольных сумм (MD5). Файлы могут иметь
# одинаковое содержимое, но отличаться именами. Скрипт должен вывести группы
# имен обнаруженных файлов-дубликатов.


import os
import hashlib


def find_md5(patch):
    with open(patch, 'r') as f:
        content = f.read()
    checksum = hashlib.md5(content.encode('utf-8')).hexdigest()
    return checksum

# dirPatch = str(input("Enter the path to the directory:\n"))
folderPatch = "E:\\Мои документы\\Питон\\Lab2\\task2 test dir"

files = [folderPatch + '\\' + file for file in os.listdir(folderPatch)
         if os.path.isfile(folderPatch + '\\' + file)]
folders = [folderPatch + '\\' + file for file in os.listdir(folderPatch)
           if os.path.isdir(folderPatch + '\\' + file)]

files = files + [folder + '\\' + file for folder in folders
                 for file in os.listdir(folder) if os.path.isfile(folder + '\\' + file)]
# контрольные суммы у файлов с разных папок отличаются
fileAndHSum = {file: find_md5(file) for file in files}

hashSumList = list(fileAndHSum.values())
duplicateHashSum = {hashSum for hashSum in hashSumList if hashSumList.count(hashSum) >= 2}

for file in fileAndHSum:
    if fileAndHSum[file] in duplicateHashSum:
        print(file)
