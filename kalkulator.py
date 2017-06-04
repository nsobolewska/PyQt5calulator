import sys
from PyQt5.QtWidgets import *
# QMainWindow, QPushButton, QApplication, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, Qt

class Window(QMainWindow):

    enlargeCount = 0
    licznik = 0
    liczba = 0
    numbers = []
    flagNew = 0
    numbers.append(0)

    # if flag == 1 then addition
    # if flag == 2 then substract
    # if flag == 3 then multiplication
    # if flag == 4 then division
    flag = 0
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(100,100,500,500)
        self.okno = QWidget(self)
        self.setCentralWidget(self.okno)
        self.mainLayout = QHBoxLayout()
        self.gridLayout = QGridLayout()
        self.okno.setLayout(self.mainLayout)
        self.setWindowTitle("Kalkulator")
        # menu
        #extractAction = QtGui.QActionEvent('&Menu',self)

        self.home()
        self.mainLayout.addLayout(self.gridLayout)
        checkbox = QCheckBox('Zwieksz okno',self)
        checkbox.move(10,30)
        checkbox.stateChanged.connect(self.enlarge)
        self.mainLayout.addWidget(checkbox, alignment=Qt.AlignCenter)
        print(self.style().objectName())
        self.StyleChoice = QLabel("Windows Vista",self)
        combobox = QComboBox(self)
        combobox.addItem("motif")
        combobox.addItem("Windows")
        combobox.addItem("cde")
        combobox.addItem("Plastique")
        combobox.addItem("Cleanlooks")
        combobox.addItem("windowsvista")

        # self.mainLayout.addWidget(self.StyleChoice, aligment = Qt.AlignTop)
        self.mainLayout.addWidget(combobox, alignment = Qt.AlignTop)
        combobox.activated[str].connect(self.stylechoice)

        self.show()

        self.initUI()

    def stylechoice(self,text):
        self.StyleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def enlarge(self,state):
        if self.enlargeCount == 0:
            self.setGeometry(50,50,1000,1000)
            self.enlargeCount = 1
        else:
            self.setGeometry(50,50,500,500)
            self.enlargeCount = 0


#menu
    def initUI(self):
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        enlargeAction = QAction('&Enlarge', self)
        enlargeAction.setShortcut('Ctrl+L')
        enlargeAction.setStatusTip('Enlarge window')
        enlargeAction.triggered.connect(self.enlarge)

        # self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(enlargeAction)
        fileMenu.addAction(exitAction)

        self.show()


# buttons
    def home(self):

        btn0 = QPushButton('0',self)
        btn0.clicked.connect(self.on_click0)
        btn0.resize(btn0.minimumSizeHint())
        # btn0.move(100, 50)
        self.gridLayout.addWidget(btn0,0,0)

        btn1 = QPushButton('1',self)
        btn1.clicked.connect(self.on_click1)
        btn1.resize(btn1.minimumSizeHint())
        self.gridLayout.addWidget(btn1,0,1)
        # btn1.move(100,100)

        btn2 = QPushButton('2',self)
        btn2.clicked.connect(self.on_click2)
        btn2.resize(btn2.minimumSizeHint())
        self.gridLayout.addWidget(btn2,0,2)
        # btn2.move(100,150)

        btn3 = QPushButton('3',self)
        btn3.clicked.connect(self.on_click3)
        btn3.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn3,1,0)
        # btn3.move(100,200)

        btn4 = QPushButton('4',self)
        btn4.clicked.connect(self.on_click4)
        btn4.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn4,1,1)
        # btn4.move(100, 250)

        btn5 = QPushButton('5',self)
        btn5.clicked.connect(self.on_click5)
        btn5.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn5,1,2)
        # btn5.move(100, 300)

        btn6 = QPushButton('6',self)
        btn6.clicked.connect(self.on_click6)
        btn6.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn6,2,0)
        # btn6.move(100, 350)

        btn7 = QPushButton('7',self)
        btn7.clicked.connect(self.on_click7)
        btn7.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn7,2,1)
        # btn7.move(100, 400)

        btn8 = QPushButton('8',self)
        btn8.clicked.connect(self.on_click8)
        btn8.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn8,2,2)
        # btn8.move(100, 450)

        btn9 = QPushButton('9',self)
        btn9.clicked.connect(self.on_click9)
        btn9.resize(btn3.minimumSizeHint())
        self.gridLayout.addWidget(btn9,3,0)
        # btn9.move(100, 500)

        btnp = QPushButton('+',self)
        btnp.clicked.connect(self.on_clickp)
        btnp.resize(btnp.minimumSizeHint())
        self.gridLayout.addWidget(btnp,0,3)
        # btnp.move(200, 500)

        btnm = QPushButton('-',self)
        btnm.clicked.connect(self.on_clickm)
        btnm.resize(btnm.minimumSizeHint())
        self.gridLayout.addWidget(btnm,1,3)
        # btnm.move(200, 450)

        btnmn = QPushButton('*',self)
        btnmn.clicked.connect(self.on_clickmn)
        btnmn.resize(btnmn.minimumSizeHint())
        self.gridLayout.addWidget(btnmn,2,3)
        # btnmn.move(200, 400)

        btndz = QPushButton('/',self)
        btndz.clicked.connect(self.on_clickdz)
        btndz.resize(btndz.minimumSizeHint())
        self.gridLayout.addWidget(btndz,3,3)
        # btndz.move(200, 350)

        btneq = QPushButton('=',self)
        btneq.clicked.connect(self.on_clickeq)
        btneq.resize(btndz.minimumSizeHint())
        self.gridLayout.addWidget(btneq,3,2)
        # btneq.move(200, 300)


    def on_click0(self):
        self.liczba = self.liczba*10 + 0
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click1(self):
        self.liczba = self.liczba * 10 + 1
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click2(self):
        self.liczba = self.liczba * 10 + 2
        print(self.liczba)

    def on_click3(self):

        self.liczba = self.liczba * 10 + 3
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click4(self):
        self.liczba = self.liczba * 10 + 4
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click5(self):
        self.liczba = self.liczba * 10 + 5
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click6(self):
        self.liczba = self.liczba * 10 + 6
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click7(self):
        self.liczba = self.liczba * 10 + 7
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click8(self):
        self.liczba = self.liczba * 10 + 8
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_click9(self):
        self.liczba = self.liczba * 10 + 9
        print(self.liczba)
        # self.licznik = self.licznik + 1

    def on_clickm(self):
        self.flagNew = self.flag
        self.flag = 2
        result = 0
        # first = self.numbers[-2]
        if self.licznik == 0:
            self.numbers.append(self.liczba)

        if self.flagNew == 1:
            result = self.numbers[-1] + self.liczba
            self.numbers.append(result)
        if self.flagNew == 2:
            result = self.numbers[-1] - self.liczba
            # print(self.numbers[-1],' - ',self.liczba,' = ',result)
            self.numbers.append(result)
        if self.flagNew == 3:
            result = self.numbers[-1] * self.liczba
            self.numbers.append(result)
        if self.flagNew == 4:
            result = self.numbers[-1] / self.liczba
            self.numbers.append(result)

        # self.numbers.append(self.liczba)
        self.liczba = 0


        print('wynik',self.numbers[-1])
        # print(self.liczba)
        self.licznik = self.licznik + 1

    def on_clickp(self):
        self.flagNew = self.flag
        self.flag = 1
        result = 0
        # first = self.numbers[-2]
        if self.licznik == 0:
            self.numbers.append(self.liczba)

        if self.flagNew == 1:
            result = self.numbers[-1] + self.liczba
            self.numbers.append(result)
        if self.flagNew == 2:
            result = self.numbers[-1] - self.liczba
            print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
            self.numbers.append(result)
        if self.flagNew == 3:
            result = self.numbers[-1] * self.liczba
            self.numbers.append(result)
        if self.flagNew == 4:
            result = self.numbers[-1] / self.liczba
            self.numbers.append(result)

        # self.numbers.append(self.liczba)
        self.liczba = 0

        print('wynik', self.numbers[-1])
        # print(self.liczba)
        self.licznik = self.licznik + 1

    def on_clickmn(self):
        self.flagNew = self.flag
        self.flag = 3
        result = 0
        # first = self.numbers[-2]
        if self.licznik == 0:
            self.numbers.append(self.liczba)

        if self.flagNew == 1:
            result = self.numbers[-1] + self.liczba
            self.numbers.append(result)
        if self.flagNew == 2:
            result = self.numbers[-1] - self.liczba
            # print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
            self.numbers.append(result)
        if self.flagNew == 3:
            result = self.numbers[-1] * self.liczba
            self.numbers.append(result)
        if self.flagNew == 4:
            result = self.numbers[-1] / self.liczba
            self.numbers.append(result)

        # self.numbers.append(self.liczba)
        self.liczba = 0

        print('wynik', self.numbers[-1])
        # print(self.liczba)
        self.licznik = self.licznik + 1

    def on_clickdz(self):
        self.flagNew = self.flag
        self.flag = 4
        result = 0
        # first = self.numbers[-2]
        if self.licznik == 0:
            self.numbers.append(self.liczba)

        if self.flagNew == 1:
            result = self.numbers[-1] + self.liczba
            self.numbers.append(result)
        if self.flagNew == 2:
            result = self.numbers[-1] - self.liczba
            print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
            self.numbers.append(result)
        if self.flagNew == 3:
            result = self.numbers[-1] * self.liczba
            self.numbers.append(result)
        if self.flagNew == 4:
            result = self.numbers[-1] / self.liczba
            self.numbers.append(result)

        # self.numbers.append(self.liczba)
        self.liczba = 0

        print('wynik = ', self.numbers[-1])
        # print(self.liczba)
        self.licznik = self.licznik + 1

    def on_clickeq(self):
        self.flagNew = self.flag
        self.flag = 0
        result = 0
        if self.liczba != 0:
            if self.flagNew == 1:
                result = self.numbers[-1] + self.liczba
                self.numbers.append(result)
            if self.flagNew == 2:
                result = self.numbers[-1] - self.liczba
                print(self.numbers[-1], ' - ', self.liczba, ' = ', result)
                self.numbers.append(result)
            if self.flagNew == 3:
                result = self.numbers[-1] * self.liczba
                self.numbers.append(result)
            if self.flagNew == 4:
                result = self.numbers[-1] / self.liczba
                self.numbers.append(result)
        print('wynik = ', self.numbers[-1])
        self.liczba = 0
        self.numbers = []
        self.numbers.append(0)
        self.licznik = 0

    def close(self):
        choice = QMessageBox.question(self,'Extract',"Are you sure you want to quit?",QMessageBox.Yes|QMessageBox.No)

        if choice == QMessageBox.Yes:
            print("Zamykamy sie")
            sys.exit()
        else:
            pass

    def rozmiar_wiek(self):
        self.btn0.resize(100, 100)
        self.btn1.resize(100,100)

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()
        self.close()

def run():

    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()
