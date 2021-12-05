import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from Samolechenie import Ui_MainWindow
from Main_form import Ui_Form1
from lechenie import Ui_Form2
from vhod import Ui_MainWindow_reg
from kabinet import Ui_MainWindow_kab
from okno_samol import Ui_MainWindow_okno


class MainWindow(QMainWindow, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.samolechenie = Samolechenie()
        self.lechenie = Lechenie()
        self.setupUi(self)
        self.pushButton_yes.clicked.connect(self.yes)
        self.pushButton_no.clicked.connect(self.no)

    def yes(self):
        self.lechenie.show()

    def no(self):
        self.samolechenie.show()


class Samolechenie(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_find_pills.clicked.connect(self.pills)
        self.disease = [(self.checkBox_temp, self.checkBox_temp.isChecked()),
                        (self.checkBox_nos, self.checkBox_nos.isChecked()),
                        (self.checkBox_varikoz, self.checkBox_varikoz.isChecked()),
                        (self.checkBox_allergia, self.checkBox_allergia.isChecked()),
                        (self.checkBox_diarea, self.checkBox_diarea.isChecked()),
                        (self.checkBox_kashel_sux, self.checkBox_kashel_sux.isChecked()),
                        (self.checkBox_kashel_vlaz, self.checkBox_kashel_vlaz.isChecked()),
                        (self.checkBox_musculpain, self.checkBox_musculpain.isChecked()),
                        (self.checkBox_headpain, self.checkBox_headpain.isChecked()),
                        (self.checkBox_throatpain, self.checkBox_throatpain.isChecked()),
                        (self.checkBox_stomachpain, self.checkBox_stomachpain.isChecked()),
                        (self.checkBox_teethpain, self.checkBox_teethpain.isChecked())]
        self.profilaktic = [(self.checkBox_gripp, self.checkBox_gripp.isChecked()),
                            (self.checkBox_virus, self.checkBox_gripp.isChecked()),
                            (self.checkBox_immun, self.checkBox_gripp.isChecked()),
                            (self.checkBox_heart, self.checkBox_gripp.isChecked())]
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
        print(lst_sympt)
        self.find_pills = FindPills(lst_sympt)
        self.find_pills.show()


class FindPills(QMainWindow, Ui_MainWindow_okno):
    def __init__(self, lst_sympt):
        super().__init__()
        self.lst_sympt = lst_sympt
        self.setupUi(self)
        self.connection = sqlite3.connect('tabletochki.db')
        self.create_tablets()
        self.create_analogues()
        # self.pushButton_find_pills.clicked.connect(self.create_tablets)
        # self.pushButton_find_semiills.clicked.connect(self.create_analogues)

    def create_tablets(self):
        cursor = self.connection.cursor()
        print(str(self.lst_sympt)[1:-1])
        all_tablets = list(cursor.execute(f"""SELECT name_of_pills, for_what, dosage, cost FROM tabletka
        WHERE for_what in (SELECT id_symptom FROM symptoms 
        WHERE name in ({str(self.lst_sympt)[1:-1]}))"""))
        print(all_tablets)
        for elem in all_tablets:
            elem = [str(i) for i in elem]
            elem[1] = list(cursor.execute(f"""SELECT name FROM symptoms WHERE id_symptom = {int(elem[1])}"""))
            elem[1] = str(elem[1])[3:-4]
            st = ' - '.join(elem)
            self.listWidget.addItem(st)

    def create_analogues(self):
        cursor = self.connection.cursor()
        all_analogue = list(cursor.execute("""SELECT name_of_pills, for_what, dosage, cost FROM analogue"""))
        add = []
        for i in self.lst_sympt:
            for elem in all_analogue:
                if i == elem[1]:
                    add.append((elem[0], elem[2], elem[3]))
        self.listWidget.addItems(add)


class Lechenie(QMainWindow, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect('tabletochki.db')
        self.comboBox.setEditable(True)
        self.create_tablets()
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_back.clicked.connect(lambda: self.hide())
        self.spinBox.setValue(1)
        self.lineEdit.setText('0')

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
            self.lineEdit.setText(f'{int(self.lineEdit.text()) + int(elem)}')
        else:
            self.listWidget.addItem(self.comboBox.currentText() + f'  * {self.spinBox.value()} шт.')
            self.listWidget.setCurrentItem(self.listWidget.item(self.listWidget.count() - 1))
            elem = self.listWidget.selectedIndexes()[0].data()
            elem = elem.split(' - ')
            sum = int(elem[2][:-13]) * int(elem[2][-5])
            self.lineEdit.setText(f'{int(self.lineEdit.text()) + sum}')

    def delete(self):
        row = self.listWidget.row(self.listWidget.currentItem())
        elem = self.listWidget.selectedIndexes()[0].data()
        elem = elem.split(' - ')
        if '*' in elem[2]:
            sum = int(elem[2][:-13]) * int(elem[2][-5])
        else:
            sum = int(elem[2][:-4])
        self.lineEdit.setText(f'{int(self.lineEdit.text()) - sum}')
        self.listWidget.takeItem(row)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
