import sys
import sqlite3
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow
from Samolechenie import Ui_MainWindow
from lechenie1 import Ui_Form2
from vhod import Ui_MainWindow_reg
from kabinet import Ui_MainWindow_kab
from okno_samol1 import Ui_MainWindow_okno
from okno_prof import Ui_MainWindow_prof
from zakaz import Ui_Form_zakaz
from info import Ui_Form_info
from warning import Ui_MainWindow_warn
from rules import Ui_MainWindow_rules


class Registr(QMainWindow, Ui_MainWindow_reg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect(r'C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\tabletochki.db')
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.enter)
        self.lineEdit_3.textChanged.connect(self.change)
        self.lineEdit_4.textChanged.connect(self.change)
        self.lineEdit.textChanged.connect(self.change)

    def change(self):
        self.label_16.hide()
        self.label_17.hide()
        self.label_18.hide()
        self.label_18.setText('Такой логин уже существует!')

    def login(self):
        if self.lineEdit.text():
            cursor = self.connection.cursor()
            id_user = list(cursor.execute(f"""SELECT id_user FROM user
                            WHERE user_login = '{self.lineEdit.text()}'"""))
            if not id_user:
                cursor.execute(
                    f"""INSERT INTO user(user_login, user_password)
                     VALUES ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}')""")
                self.connection.commit()
                id_user = list(cursor.execute(f"""SELECT id_user FROM user
                                        WHERE user_login = '{self.lineEdit.text()}'"""))
                id_user = str(id_user)[2:-3]
                cursor.execute(f"""CREATE TABLE table{id_user} (
                                    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name STRING,
                                    date DATE,
                                    coast STRING, 
                                    info STRING
                                    )""")
                self.connection.commit()
                self.kabinet = Kabinet(id_user, self.lineEdit.text())
                self.kabinet.show()
                self.hide()
            else:
                self.label_18.show()
        else:
            self.label_18.setText('Логин должен содержать хотя бы 1 символ')
            self.label_18.show()

    def enter(self):
        cursor = self.connection.cursor()
        id_user = list(cursor.execute(f"""SELECT id_user FROM user
        WHERE user_login = '{self.lineEdit_4.text()}'"""))
        if not id_user:
            self.label_16.show()
        else:
            cursor = self.connection.cursor()

            right_password = list(cursor.execute(f"""SELECT user_password FROM user
            WHERE id_user = {int(str(id_user)[2:-3])}"""))
            right_password[0] = list(right_password[0])
            if self.lineEdit_3.text() == right_password[0][0]:
                self.kabinet = Kabinet(str(id_user)[2:-3], self.lineEdit_4.text())
                self.kabinet.show()
                self.hide()
            else:
                self.label_17.show()


class Kabinet(QMainWindow, Ui_MainWindow_kab):
    def __init__(self, id_user, name):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect(r'C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\tabletochki.db')
        self.user_id = id_user
        self.add_item_to_lw()
        self.name = name
        self.label.setText(f'Здравствуйте, {self.name}')
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_update.clicked.connect(self.updat)
        self.listWidget.doubleClicked.connect(self.info)

    def add_item_to_lw(self):
        cursor = self.connection.cursor()
        items = list(cursor.execute(f"""SELECT date, name, coast FROM table{self.user_id}"""))
        items = list(map(list, items))
        for elem in items:
            st = f'{elem[0]} : {elem[1]} - {elem[2]}'
            self.listWidget.insertItem(0, st)
        while self.listWidget.count() > 14:
            self.listWidget.takeItem(14)

    def info(self):
        cursor = self.connection.cursor()
        item = self.listWidget.currentItem().text()
        item = item.split(' : ')
        lst = item[1][::-1].split(' - ', maxsplit=1)
        lst = list(map(lambda x: x[::-1], lst))
        item.remove(item[1])
        item.extend(lst)
        info = list((cursor.execute(f"""SELECT info FROM table{self.user_id}
        WHERE name = '{item[2]}' AND coast = '{item[1]}' AND date = '{item[0]}'""")))
        self.infowidget = Info_Widget(info, item[1], item[0])
        self.infowidget.show()

    def yes(self):
        self.lechenie = Lechenie(self.user_id)
        self.lechenie.show()

    def no(self):
        self.warn = Warning(self.user_id)
        self.warn.show()

    def exit(self):
        self.registr = Registr()
        self.hide()
        self.registr.show()

    def updat(self):
        self.hide()
        self.kabinet = Kabinet(self.user_id, self.name)
        self.kabinet.show()


class Info_Widget(QMainWindow, Ui_Form_info):
    def __init__(self, info, cost, date):
        super().__init__()
        self.setupUi(self)
        self.info = info
        self.cost = cost
        self.date = date
        self.pushButton.clicked.connect(lambda: self.hide())
        self.dan()

    def dan(self):
        self.info[0] = list(self.info[0])
        info = self.info[0][0].split('\n')
        info.remove(info[-1])
        info.append('\n')
        info.append(f'Дата заказа: {self.date}')
        info.append(f"Общая сумма заказа: {self.cost}")
        self.listWidget.insertItems(0, info)


class Samolechenie(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.pushButton_find_pills.clicked.connect(self.pills)
        self.pushButton_find_semiills.clicked.connect(self.prevention)
        self.prevent = [self.checkBox_gripp,
                        self.checkBox_virus,
                        self.checkBox_immun,
                        self.checkBox_heart]
        self.disease = [self.checkBox_temp,
                        self.checkBox_nos,
                        self.checkBox_varikoz,
                        self.checkBox_allergia,
                        self.checkBox_diarea,
                        self.checkBox_kashel_sux,
                        self.checkBox_kashel_vlaz,
                        self.checkBox_musculpain,
                        self.checkBox_headpain,
                        self.checkBox_throatpain,
                        self.checkBox_stomachpain,
                        self.checkBox_teethpain]


    def pills(self):
        lst_sympt = []
        for elem in self.disease:
            if elem.isChecked():
                lst_sympt.append(elem.text())
        self.find_pills = FindPills(lst_sympt, self.user_id)
        self.find_pills.show()

    def prevention(self):
        lst_prof = []
        for elem in self.prevent:
            if elem.isChecked():
                lst_prof.append(elem.text())
        self.prof = Prevention(lst_prof, self.user_id)
        self.prof.show()


class Rules(QMainWindow, Ui_MainWindow_rules):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hiding)

    def hiding(self):
        self.hide()


class Warning(QMainWindow, Ui_MainWindow_warn):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.pushButton_2.hide()
        self.checkBox.clicked.connect(self.showing)
        self._closable = False

        self.pushButton_2.clicked.connect(self.hiding)
        self.pushButton.clicked.connect(self.inf)

    def closeEvent(self, evnt):
        if self._closable:
            super(Warning, self).closeEvent(evnt)
        else:
            evnt.ignore()

    def showing(self):
        self.pushButton_2.show()

    def hiding(self):
        self.samolechenie = Samolechenie(self.user_id)
        self.samolechenie.show()
        self.hide()

    def inf(self):
        self.rule = Rules()
        self.rule.show()


class FindPills(QMainWindow, Ui_MainWindow_okno):
    def __init__(self, lst_sympt, user_id):
        super().__init__()
        self.lst_sympt = lst_sympt
        self.user_id = user_id
        self.setupUi(self)
        self.connection = sqlite3.connect(r'C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\tabletochki.db')
        self.create_tablets()
        self.create_analogues()
        self.pushButton_save_2.clicked.connect(self.count)
        self.pushButton_2.clicked.connect(self.exit)
        self.pushButton_save.clicked.connect(self.save)

    def create_tablets(self):
        cursor = self.connection.cursor()
        all_tablets = list(cursor.execute(f"""SELECT name_of_pills, for_what, dosage, cost FROM tabletka
        WHERE for_what in (SELECT id_symptom FROM symptoms 
        WHERE name in ({str(self.lst_sympt)[1:-1]}))"""))
        for elem in all_tablets:
            elem = [str(i) for i in elem]
            elem[1] = list(cursor.execute(f"""SELECT name FROM symptoms WHERE id_symptom = {int(elem[1])}"""))
            elem[1] = str(elem[1])[3:-4]
            elem[3] += ' руб.'
            st = ' - '.join(elem)
            self.listWidget.addItem(st)

    def create_analogues(self):
        cursor = self.connection.cursor()
        all_analogue = list(cursor.execute("""SELECT id_analogue, name_of_pills, for_what, dosage, cost FROM analogue"""))
        add = []
        id_analog = list(cursor.execute(f"""SELECT id_analogue FROM analogue
        WHERE for_what in (SELECT id_symptom FROM symptoms 
        WHERE name in ({str(self.lst_sympt)[1:-1]}))"""))
        for i in id_analog:
            for elem in all_analogue:
               if i[0] == elem[0]:
                    symp = list(cursor.execute(f"""SELECT name FROM symptoms WHERE id_symptom = {int(elem[2])}"""))
                    symp = str(symp)[3:-4]
                    add.append(f'{elem[1]} - {symp} - {elem[3]} - {elem[4]} руб. ')
        add = list(map(lambda x: str(x), add))
        self.listWidget_2.addItems(add)

    def count(self):
        noun = [x.text().split(' - ') for x in self.listWidget.selectedItems()]
        noun1 = [x.text().split(' - ') for x in self.listWidget_2.selectedItems()]
        counter = []
        for i in noun:
            counter.append(int(i[3][:-5]))
        for i in noun1:
            counter.append(int(i[3][:-5]))
        count = sum(counter)
        self.lineEdit.setText(f'{count} руб.')

    def exit(self):
        self.hide()

    def save(self):
        if self.lineEdit.text():
            items = [x.text() for x in self.listWidget.selectedItems()]
            items.extend([x.text() for x in self.listWidget_2.selectedItems()])
            self.zakaz = Zakaz(items, self.user_id, self.lineEdit.text())
            self.zakaz.show()


class Prevention(QMainWindow, Ui_MainWindow_prof):
    def __init__(self, lst_prof, user_id):
        super().__init__()
        self.lst_prof = lst_prof
        self.user_id = user_id
        self.setupUi(self)
        self.connection = sqlite3.connect(r'C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\tabletochki.db')
        self.create_prevents()
        self.pushButton_itog.clicked.connect(self.count)
        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_save.clicked.connect(self.save)

    def create_prevents(self):
        cursor = self.connection.cursor()
        all_prevents = list(cursor.execute("""SELECT id, name, for_what, dosage, cost FROM prevention"""))
        add = []
        id = list(cursor.execute(f"""SELECT id FROM prevention
                WHERE for_what in (SELECT id_symptom FROM symptoms 
                WHERE name in ({str(self.lst_prof)[1:-1]}))"""))
        for i in id:
            for elem in all_prevents:
                if i[0] == elem[0]:
                    symp = list(cursor.execute(f"""SELECT name FROM symptoms
                    WHERE id_symptom in (SELECT for_what FROM prevention WHERE for_what = {int(elem[2])})"""))
                    symp = str(symp)[3:-4]
                    add.append(f'{elem[1]} - {symp} - {elem[3]} - {elem[4]} руб.')
        add = list(map(lambda x: str(x), add))
        self.listWidget.addItems(add)

    def count(self):
        noun = [x.text().split(' - ') for x in self.listWidget.selectedItems()]
        counter = []
        for i in noun:
            counter.append(int(i[3][:-5]))
        count = sum(counter)
        self.lineEdit.setText(f'{count} руб.')

    def exit(self):
        self.hide()

    def save(self):
        items = [x.text() for x in self.listWidget.selectedItems()]
        self.zakaz = Zakaz(items, self.user_id, self.lineEdit.text())
        self.zakaz.show()


class Lechenie(QMainWindow, Ui_Form2):
    def __init__(self, user_id):
        super().__init__()
        self.setupUi(self)
        self.user_id = user_id
        self.connection = sqlite3.connect(r'C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\tabletochki.db')
        self.comboBox.setEditable(True)
        self.create_tablets()
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_back.clicked.connect(lambda: self.hide())
        self.pushButton_create.clicked.connect(self.create_order)
        self.spinBox.setValue(1)
        self.lineEdit.setText('0 руб.')

    def create_tablets(self):
        cursor = self.connection.cursor()
        all_tablets = list(cursor.execute("""SELECT name_of_pills, dosage, cost FROM tabletka"""))
        all_analogue = list(cursor.execute("""SELECT name_of_pills, dosage, cost FROM analogue"""))
        lst_all = all_tablets + all_analogue
        for elem in lst_all:
            elem = list(elem)
            elem[2] = str(elem[2]) + ' руб'
            st = ' - '.join(elem)
            self.comboBox.addItem(st)

    def add(self):
        if int(self.spinBox.text()) == 1:
            self.listWidget.addItem(self.comboBox.currentText())
            self.listWidget.setCurrentItem(self.listWidget.item(self.listWidget.count() - 1))
            elem = self.listWidget.selectedIndexes()[0].data()
            elem = elem.split(' - ')
            elem = elem[2][:-4]
            self.lineEdit.setText(f'{int(self.lineEdit.text()[:-5]) + int(elem)} руб.')
        else:
            self.listWidget.addItem(self.comboBox.currentText() + f'  * {self.spinBox.value()} шт.')
            self.listWidget.setCurrentItem(self.listWidget.item(self.listWidget.count() - 1))
            elem = self.listWidget.selectedIndexes()[0].data()
            elem = elem.split(' - ')
            sum = int(elem[2][:-13]) * int(elem[2][-5])
            self.lineEdit.setText(f'{int(self.lineEdit.text()[:-5]) + sum} руб.')

    def delete(self):
        row = self.listWidget.row(self.listWidget.currentItem())
        if row != -1:
            elem = self.listWidget.selectedIndexes()[0].data()
            elem = elem.split(' - ')
            if '*' in elem[2]:
                sum = int(elem[2][:-13]) * int(elem[2][-5])
            else:
                sum = int(elem[2][:-4])
            self.lineEdit.setText(f'{int(self.lineEdit.text()[:-5]) - sum} руб.')
            self.listWidget.takeItem(row)

    def create_order(self):
        items = [self.listWidget.item(row).text() for row in range(self.listWidget.count())]
        self.zakaz = Zakaz(items, self.user_id, self.lineEdit.text())
        self.zakaz.show()


class Zakaz(QMainWindow, Ui_Form_zakaz):
    def __init__(self, items, user_id, coast):
        super().__init__()
        self.setupUi(self)
        self.connect = sqlite3.connect(r'C:\Users\danya\PycharmProjects\Project_12.21\project_tabletka\tabletochki.db')
        self.items = items
        self.user_id = user_id
        self.coast = coast
        self.pushButton_ok.clicked.connect(self.ok)
        self.pushButton_cancel.clicked.connect(lambda: self.hide())
        self.lineEdit.textChanged.connect(lambda: self.label_2.hide())

    def ok(self):
        if self.lineEdit.text():
            st = ''
            for elem in self.items:
                st += elem + '\n'
            cursor = self.connect.cursor()
            names = list(cursor.execute(f"""SELECT name FROM table{self.user_id}"""))
            names = list(map(lambda x: str(x)[2:-3], names))
            if self.lineEdit.text() in names:
                self.label_2.show()
            else:
                cursor.execute(f"""INSERT INTO table{self.user_id} (name, date, coast, info)
                     VALUES ('{self.lineEdit.text()}', '{datetime.now().date()}', '{self.coast}', '{st}')""")
                self.connect.commit()
                self.hide()


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    ex.show()
    sys.exit(app.exec())
