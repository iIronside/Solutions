# Создайте графическую оболочку для скрипта, написанного
# в ходе выполнения задания № 4 лабораторной работы № 2,
# в виде диалогового окна.

import sys
import os
import re
import datetime
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Notepad(QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()
        self.check_log_file()

    def initUI(self):

        # Create Actions for menus
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open a file')
        open_action.triggered.connect(self.openFile)

        close_action = QAction('Close', self)
        close_action.setShortcut('Ctrl+Q')
        close_action.setStatusTip('Close Notepad')
        close_action.triggered.connect(self.close)

        export_action = QAction('Экспорт', self)
        export_action.setStatusTip('Exsport')
        export_action.triggered.connect(self.exportText)

        add_action = QAction('Добавить в лог', self)
        add_action.setStatusTip('Add')
        add_action.triggered.connect(self.add_to_log)

        view_action = QAction('Просмотр', self)
        view_action.setStatusTip('View')
        view_action.triggered.connect(self.view_log)

        # Create Root Menus
        file_bar = self.menuBar()
        log_bar = self.menuBar()

        file_menu = file_bar.addMenu('&File')
        file_menu.addAction(open_action)
        file_menu.addAction(close_action)

        log_menu = log_bar.addMenu('&Log')
        log_menu.addAction(export_action)
        log_menu.addAction(view_action)
        log_menu.addAction(add_action)

        self.textEdit = QTextEdit(self)
        self.textEdit.setFocus()
        self.textEdit.setReadOnly(True)

        self.resize(450, 400)
        self.setWindowTitle('Notepad')
        self.setCentralWidget(self.textEdit)
        self.show()

    def view_log(self):
        buttonReply = QMessageBox.question(self, 'Open log', "Вы действительно хотите открыть лог?"
                                               "Данные последних поисков будут потеряны!",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            filename = os.getcwd() + '\\' + 'log.txt'
            with open(filename, 'r') as f:
                my_text = f.read()
                print('111')
                self.textEdit.append(my_text)

    def check_log_file(self):
        if os.path.exists(os.getcwd() + '\\' + 'log.txt') is False:
            QMessageBox.question(self, 'The log file is not found',
                                 "Файл лога не найден. Файл будет создан автоматически.",
                                 QMessageBox.Ok)
            open(os.getcwd() + '\\' + 'log.txt', 'wt').close()

    def add_to_log(self):
        filename = os.getcwd() + '\\' + 'log.txt'
        with open(filename, 'a') as f:
            my_text = self.textEdit.toPlainText()
            f.write(my_text)

    def exportText(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.textEdit.toPlainText()
            f.write(my_text)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))

        fh = ''

        if QFile.exists(filename):
            fh = QFile(filename)

        if not fh.open(QFile.ReadOnly):
            QtGui.qApp.quit()

        data = fh.readAll()
        codec = QTextCodec.codecForUtfText(data)
        unistr = codec.toUnicode(data)
        result = re.findall(r'\d{3}.\d{3}.\d.\d{2}', unistr)

        # Windiw name
        tmp = ('Text Edit: %s' % filename)
        self.setWindowTitle(tmp)

        # Fill the window
        self.textEdit.append(filename + ' ' + datetime.datetime.now(tz=None).strftime("%H:%M %d-%m-%Y"))
        for s in result:
            self.textEdit.append(s)


def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()