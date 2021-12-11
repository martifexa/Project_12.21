import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from Samolechenie import Ui_MainWindow
from Main_form import Ui_Form1
from lechenie1 import Ui_Form2
from vhod import Ui_MainWindow_reg
from kabinet import Ui_MainWindow_kab
from okno_samol1 import Ui_MainWindow_okno
from okno_prof import Ui_MainWindow_prof


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
        self.find_pills = FindPills(lst_sympt)
        self.find_pills.show()

    def prevention(self):
        lst_prof = []
        for elem in self.prevent:
            if elem.isChecked():
                lst_prof.append(elem.text())
        self.prof = Prevention(lst_prof)
        self.prof.show()


class FindPills(QMainWindow, Ui_MainWindow_okno):
    def __init__(self, lst_sympt):
        super().__init__()
        self.lst_sympt = lst_sympt
        self.setupUi(self)
        self.connection = sqlite3.connect('tabletochki.db')
        self.create_tablets()
        self.create_analogues()
        self.pushButton_save_2.clicked.connect(self.count)
        self.pushButton_2.clicked.connect(self.exit)

    def create_tablets(self):
        cursor = self.connection.cursor()
        all_tablets = list(cursor.execute(f"""SELECT name_of_pills, for_what, dosage, cost FROM tabletka
        WHERE for_what in (SELECT id_symptom FROM symptoms 
        WHERE name in ({str(self.lst_sympt)[1:-1]}))"""))
        for elem in all_tablets:
            elem = [str(i) for i in elem]
            elem[1] = list(cursor.execute(f"""SELECT name FROM symptoms WHERE id_symptom = {int(elem[1])}"""))
            elem[1] = str(elem[1])[3:-4]
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
                    add.append(f'{elem[1]} - {symp} - {elem[3]} - {elem[4]} ')
        add = list(map(lambda x: str(x), add))
        self.listWidget_2.addItems(add)

    def count(self):
        noun = [x.text().split(' - ') for x in self.listWidget.selectedItems()]
        noun1 = [x.text().split(' - ') for x in self.listWidget_2.selectedItems()]
        counter = []
        for i in noun:
            counter.append(int(i[3]))
        for i in noun1:
            counter.append(int(i[3]))
        count = sum(counter)
        self.lineEdit.setText(f'{count} руб.')

    def exit(self):
        self.hide()


class Prevention(QMainWindow, Ui_MainWindow_prof):
    def __init__(self, lst_prof):
        super().__init__()
        self.lst_prof = lst_prof
        self.setupUi(self)
        self.connection = sqlite3.connect('tabletochki.db')
        self.create_prevents()
        self.pushButton_itog.clicked.connect(self.count)
        self.pushButton_3.clicked.connect(self.exit)

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
                    add.append(f'{elem[1]} - {symp} - {elem[3]} - {elem[4]} ')
        add = list(map(lambda x: str(x), add))
        self.listWidget.addItems(add)

    def count(self):
        noun = [x.text().split(' - ') for x in self.listWidget.selectedItems()]
        counter = []
        for i in noun:
            counter.append(int(i[3]))
        count = sum(counter)
        self.lineEdit.setText(f'{count} руб.')

    def exit(self):
        self.hide()


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
