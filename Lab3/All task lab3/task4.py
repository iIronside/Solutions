# Напишите простой класс StringFormatter для форматирования строк со следующим функционалом:
# – удаление всех слов из строки, длина которых меньше n букв;
# – замена всех цифр в строке на знак «*»;
# – вставка по одному пробелу между всеми символами в строке;
# – сортировка слов по размеру;
# – сортировка слов в лексикографическом порядке.

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


class Parser(object):
    def __init__(self):
        self.__string = ''

    def fill(self, str):
        self.__string = str

    def get_string(self):
        return self.__string

    def remove_short(self, lentch):
        wordsList = self.__string.split(' ')
        wordsList = [word for word in wordsList if len(word) > lentch]
        self.__string = ' '.join(wordsList)

    def replace_numbers(self):
        letterList = ['*' if letter.isdigit() else letter for letter in self.__string]
        self.__string = ''.join(letterList)

    def insert_space(self):
        symbol_list = [symbol for symbol in self.__string]
        self.__string = ' '.join(symbol_list)

    def number_sort(self):
        sort_listNum = self.__string.split(' ')
        sort_listNum.sort(key=lambda item: len(item), reverse=True)
        self.__string = ' '.join(sort_listNum)

    def lexical_sort(self):
        sort_listLex = self.__string.split(' ')
        sort_listLex.sort()
        self.__string = ' '.join(sort_listLex)


class ParserForm(QMainWindow):

    def __init__(self):
        super(ParserForm, self).__init__()
        self.line = Parser()
        self.initUI()

    def initUI(self):

        # Create line edits

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(80, 15)
        self.textbox1.resize(300, 20)

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(80, 275)
        self.textbox2.resize(300, 20)

        # Create spin box
        self.spin_box = QSpinBox(self)
        self.spin_box.move(270, 48)
        self.spin_box.resize(40 ,20)

        # Create  labels
        label1 = QLabel('Строка:', self)
        label1.move(10, 10)

        label2 = QLabel('букв', self)
        label2.move(320, 42)

        label3 = QLabel('Результат:', self)
        label3.move(10, 270)


        # Create format button
        self.format_btn = QPushButton('Форматировать', self)
        self.format_btn.move(80, 230)
        self.format_btn.resize(290, 30)
        self.format_btn.clicked.connect(self.parsing)

        # Create check boxs
        self.delete_chcBox = QCheckBox('Удалить слова размером меньше', self)
        self.delete_chcBox.move(80, 50)
        self.delete_chcBox.resize(190, 15)

        self.replace_chcBox = QCheckBox('Заменить все цифры на *', self)
        self.replace_chcBox.move(80, 80)
        self.replace_chcBox.resize(190, 15)

        self.insert_chcBox = QCheckBox('Вставить пробел мужду символами', self)
        self.insert_chcBox.move(80, 110)
        self.insert_chcBox.resize(190, 15)

        self.sort_chcBox = QCheckBox('Сортировать слова в строке', self)
        self.sort_chcBox.move(80, 140)
        self.sort_chcBox.resize(190, 15)

        # Create radio buttons
        self.size_radBtn = QRadioButton('По размеру', self)
        self.size_radBtn.move(120, 170)
        self.size_radBtn.resize(80, 15)

        self.lexis_radBtn = QRadioButton('Лексикографически', self)
        self.lexis_radBtn.move(120, 200)
        self.lexis_radBtn.resize(120, 15)

        # Create  form
        self.setWindowTitle('Parser')
        self.resize(420, 330)
        self.show()

    @pyqtSlot()
    def parsing(self):
        #num = self.spin_box.value() *???
        self.line.fill(self.textbox1.text())  # read and fill

        if self.delete_chcBox.isChecked():
            self.line.remove_short(5)  # *???

        if self.replace_chcBox.isChecked():
            self.line.replace_numbers()

        if self.sort_chcBox.isChecked():
            if self.size_radBtn.isChecked():
                self.line.number_sort()
            if self.lexis_radBtn.isChecked():
                self.line.lexical_sort()

        if self.insert_chcBox.isChecked():
            self.line.insert_space()

        self.textbox2.setText(self.line.get_string()) #textboxValue


def main():
    app = QApplication(sys.argv)
    parser = ParserForm()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()