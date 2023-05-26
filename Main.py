import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi

db = sqlite3.connect('kurs.db')
cur = db.cursor()

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)


    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
        print("Successfully logged in with email: ", email, "and password:", password)
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi("menu.ui",self)
        self.corebutton.clicked.connect(self.connection)
        self.workerbutton.clicked.connect(self.connection2)
        self.productbutton.clicked.connect(self.connection5)
        self.subscribersbutton.clicked.connect(self.connection4)
        self.subscribebutton.clicked.connect(self.connection3)

    def connection(self):
        core = Core()
        widget.addWidget(core)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def connection2(self):
        worker = Worker()
        widget.addWidget(worker)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def connection3(self):
        subscribe = Subscribe()
        widget.addWidget(subscribe)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def connection4(self):
        subscribers = Subscribers()
        widget.addWidget(subscribers)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def connection5(self):
        product = Product()
        widget.addWidget(product)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Core(QDialog): #Корреспонденция белая
    def __init__(self):
        super(Core, self).__init__()
        loadUi("core.ui", self)
        self.backbutton.clicked.connect(self.gotocreate)
        self.openbutton1.clicked.connect(self.otk)

    def otk(self):
        data = cur.execute("select * from core")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        self.tablotable.setColumnCount(len(col_name))
        self.tablotable.setHorizontalHeaderLabels(col_name)
        self.tablotable.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tablotable.setRowCount(self.tablotable.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tablotable.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tablotable.resizeColumnsToContents()

    def gotocreate(self):
        menu = Menu()
        widget.addWidget( menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Worker(QDialog): # Работники оранжевый
    def __init__(self):
        super(Worker, self).__init__()
        loadUi("worker.ui", self)
        self.backbutton.clicked.connect(self.gotocreate)
        self.openbutton2.clicked.connect(self.otk2)

    def otk2(self):
            data = cur.execute("select * from worker")
            col_name = [i[0] for i in data.description]
            data_rows = data.fetchall()
            self.tablotable.setColumnCount(len(col_name))
            self.tablotable.setHorizontalHeaderLabels(col_name)
            self.tablotable.setRowCount(0)
            for i, row in enumerate(data_rows):
                self.tablotable.setRowCount(self.tablotable.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tablotable.setItem(i, j, QTableWidgetItem(str(elem)))
            self.tablotable.resizeColumnsToContents()

    def gotocreate(self):
        menu = Menu()
        widget.addWidget( menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Product(QDialog): # Издание синий
    def __init__(self):
        super(Product, self).__init__()
        loadUi("product.ui", self)
        self.backbutton.clicked.connect(self.gotocreate)
        self.openbutton3.clicked.connect(self.otk3)

    def otk3(self):
        data = cur.execute("select * from product")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        self.tablotable.setColumnCount(len(col_name))
        self.tablotable.setHorizontalHeaderLabels(col_name)
        self.tablotable.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tablotable.setRowCount(self.tablotable.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tablotable.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tablotable.resizeColumnsToContents()

    def gotocreate(self):
        menu = Menu()
        widget.addWidget( menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Subscribe(QDialog): # Подписки темно синий
    def __init__(self):
        super(Subscribe, self).__init__()
        loadUi("subscribe.ui", self)
        self.backbutton.clicked.connect(self.gotocreate)
        self.openbutton4.clicked.connect(self.otk4)

    def otk4(self):
        data = cur.execute("select * from subscribe")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        self.tablotable.setColumnCount(len(col_name))
        self.tablotable.setHorizontalHeaderLabels(col_name)
        self.tablotable.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tablotable.setRowCount(self.tablotable.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tablotable.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tablotable.resizeColumnsToContents()

    def gotocreate(self):
        menu = Menu()
        widget.addWidget( menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Subscribers(QDialog): # Подписчики красные
    def __init__(self):
        super(Subscribers, self).__init__()
        loadUi("subscribers.ui", self)
        self.backbutton.clicked.connect(self.gotocreate)
        self.openbutton.clicked.connect(self.otk5)
        self.addbutton.clicked.connect(self.insert)
        self.deletebutton.clicked.connect(self.delete)
        self.safebutton.clicked.connect(self.safe)
        self.poiskbutton.clicked.connect(self.poisk)
    def otk5(self):
        self.conn = sqlite3.connect('kurs.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from subscribers")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        self.tablotable.setColumnCount(len(col_name))
        self.tablotable.setHorizontalHeaderLabels(col_name)
        self.tablotable.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.tablotable.setRowCount(self.tablotable.rowCount()+1)
            for j, elem in enumerate(row):
                self.tablotable.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tablotable.resizeColumnsToContents()

    def update_tablotable(self, query="select * from subscribers"):
        try:
            cur = self.conn.cursor()
            data = cur.execute(query).fetchall()
        except Exception as e:
            print(f"Проблемы с подключением к БД. {e}")
            return e
        self.tablotable.setRowCount(0)
        for i, row in enumerate(data):
            self.tablotable.setRowCount(self.tablotable.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tablotable.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tablotable.resizeColumnsToContents()

    def insert(self):
        row = [self.lefam.text(), self.lename.text(), self.lefather.text(), self.lephone.text(),
               self.lestaff.text(), self.leemail.text()]
        try:
            cur = self.conn.cursor()

            cur.execute(f"""insert into subscribers (fam, name, father, phone, home, email)
            values('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}')""")
            self.conn.commit()
            cur.close()

        except Exception as e:
            print("Не смогли добавить запись.")
            return e
        self.update_tablotable()

    def delete(self):
        row = self.tablotable.currentRow()
        num = self.tablotable.item(row, 0).text()
        try:
            cur = self.conn.cursor()
            cur.execute(f"delete from subscribers where id = {num}")
            self.conn.commit()
            cur.close()
        except Exception as e:
            print("Не смогли удалить запись.")
            return e
        self.update_tablotable()

    def poisk(self):
        cur = self.conn.cursor()
        cur.execute(f"select from subscribers where id = :id")
        model.bindValue(":id", 42);
        model.exect();
        Qvariant data = model.data(model.index(0, 0));


    def gotocreate(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=Login()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(760)
    widget.setFixedHeight(620)
    widget.show()
    app.exec_()