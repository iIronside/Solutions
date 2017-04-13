# Напишите скрипт reorganize.py, который в директории --source создает
# две директории: Archive и Small. В первую директорию помещаются файлы
# с датой изменения, отличающейся от текущей даты на количество дней
# более параметра --days (т.е. относительно старые файлы). Во вторую -
# – все файлы размером меньше параметра --size байт. Каждая директория
# должна создаваться только в случае, если найден хотя бы один файл,
# который должен быть в нее помещен.

import os
import shutil

size = 5000000  # 5Mb
days = 432000  # 5 дней в секундах
sourcePath = "E:\\Мои документы\\Питон\\Lab2\\source"

try:
    fileInSource = [sourcePath + '\\' + file for file in os.listdir(sourcePath)
                    if os.path.isfile(sourcePath + '\\' + file)]

    os.chdir(sourcePath)  # изменение текущей рабочей дериктории
    for file in fileInSource:
        if os.path.getsize(file) < size:
            if os.path.exists(os.getcwd() + '\\' + 'Small'):
                shutil.move(file, os.getcwd() + '\\' + 'Small')
            else:
                os.mkdir('Small')
                shutil.move(file, os.getcwd() + '\\' + 'Small')
        elif os.path.getmtime(file) > days:
            if os.path.exists(os.getcwd() + '\\' + 'Archive'):
                shutil.move(file, os.getcwd() + '\\' + 'Archive')
            else:
                os.mkdir('Archive')
                shutil.move(file, os.getcwd() + '\\' + 'Archive')
except IOError as err:
    print(err)
