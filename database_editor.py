import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox


class Connect_db:
    def connect(self):
        con = sqlite3.connect("data/main.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM commands""").fetchall()
        con.close()
        return result


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/main.ui', self)

        self.main_button.clicked.connect(self.add)
        self.reload_button.clicked.connect(self.reload)
        self.del_button.clicked.connect(self.delete)

        self.load()

    def add(self):
        name = self.name_line.text()
        text = self.text_line.text()

        c_b = Connect_db()
        main_list = [i[1] for i in c_b.connect()]

        con = sqlite3.connect("data/main.db")
        cur = con.cursor()
        a = [(name, text)]
        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        if name in main_list:
            msg.setText("Такая команда уже есть!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        elif ' ' in name or len(name) == 0:
            msg.setText("Пустое имя или есть пробелы")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            cur.executemany("INSERT INTO commands(name, text) VALUES (?, ?);", a)
            con.commit()
            cur.close()
        self.load()
        self.reload()

    def reload(self):
        self.name_line.setText('')
        self.text_line.setText('')
        self.id_line.setText('')
        self.load()

    def delete(self):
        id = self.id_line.text()
        con = sqlite3.connect("data/main.db")
        cur = con.cursor()
        a = [(id)]

        c_b = Connect_db()
        main_list = [i[0] for i in c_b.connect()]

        msg = QMessageBox()
        msg.setWindowTitle("Ошибка")
        print(main_list)
        if int(id) not in main_list:
            msg.setText("Нет такого id!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            cur.executemany("DELETE from commands WHERE id = ?", a)
            con.commit()
            cur.close()

        self.load()
        self.reload()

    def load(self):
        con = sqlite3.connect("data/main.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM commands""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
