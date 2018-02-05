# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DNSLookup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 712)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/dnslookup/windowMain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(35, 35))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 661, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(45)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(22)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(680, 50, 381, 551))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.verticalLayoutWidget_2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(22)
        
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/dnslookup/saveCSV.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setShortcut("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(680, 10, 381, 36))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/dnslookup/searchDomain.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 610, 381, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 610, 661, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(60, 51))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionFileopen = QtWidgets.QAction("&Open File", MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/dnslookup/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFileopen.setIcon(icon3)
        self.actionFileopen.setObjectName("actionFileopen")
        self.actionOpenurl = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/dnslookup/URLopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenurl.setIcon(icon4)
        self.actionOpenurl.setObjectName("actionOpenurl")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/dnslookup/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.toolBar.addAction(self.actionFileopen)
        self.toolBar.addAction(self.actionOpenurl)
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #event
        self.actionFileopen.triggered.connect(self.onFileOpen)
        self.actionOpenurl.triggered.connect(self.onURLOpen)
        self.actionExit.triggered.connect(self.onExit)
        self.pushButton_2.clicked.connect(self.searchDomain)
        self.pushButton.clicked.connect(self.saveCSV)
        self.pushButton_3.clicked.connect(self.lookupDomain)

    def onFileOpen(self, MainWindow):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "","CSV Files (*.csv);;All Files (*)", options=options)
        self.label.setText(fileName)
        file = open(fileName, 'r')
        datas = file.readlines()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(datas)-1)
        row = 0
        for rows in datas:
            if rows[0] == "연":
                continue
            column = 0
            for columns in range(5):
                self.tableWidget.setItem(row, columns, QTableWidgetItem(rows.split(',')[column]))
                column += 1
            row += 1

    def onURLOpen(self, MainWindow):
        url = QUrl
        url = QUrl("http://whois.domaintools.com/")
        QDesktopServices.openUrl(url)

    def onExit(self, MainWindow):
        close = QMessageBox()
        close.setText("종료하시겠습니까?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Yes:
            exit(1)
        else:
            pass

    def searchDomain(self, MainWindow):
        domain = self.lineEdit.text().split(',')[-1]
        rfile = open(self.label.text(), 'r')
        datas = rfile.readlines()
        self.tableWidget_2.clearContents()
        rowPosition = self.tableWidget_2.rowCount()
        for rows in datas:
            if domain in rows:
                result = rows.split(',')[0] +','+ rows.split(',')[1] +','+ rows.split(',')[3]
                column = 0
                self.tableWidget_2.insertRow(rowPosition)
                for columns in range(3):
                    self.tableWidget_2.setItem(rowPosition, columns, QTableWidgetItem(result.split(',')[column]))
                    column += 1
                rowPosition += 1

    def saveCSV(self, MainWindow):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(None, "Save CSV File", "","CSV Files (*.csv)", options=options)
        wfile = open(fileName, 'w', newline='')
        writer = csv.writer(wfile)
        title = ['연변', '시간정보(GMT+9)', 'IP주소']
        writer.writerow(title)
        for row in range(self.tableWidget_2.rowCount()):
            rowdata = []
            for column in range(self.tableWidget_2.columnCount()):
                item = self.tableWidget_2.item(row, column).text()
                if item is not None:
                    rowdata.append(item)
                else:
                    rowdata.append('')
            writer.writerow(rowdata)

    def lookupDomain(self, MainWindow):
        import socket
        domain = self.lineEdit_2.text()
        dtoip = socket.gethostbyname(domain)
        self.lineEdit_3.setText(dtoip)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DNS Lookup"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "연변"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "시간정보(GMT+9)"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "대상 도메인"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IP주소"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "조회한 DNS 서버 IP 주소"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "연변"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "시간정보(GMT+9)"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP주소"))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_2.setText(_translate("MainWindow", "CSV 내 도메인 입력:"))
        self.label_3.setText(_translate("MainWindow", "Lookup 도메인:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionFileopen.setText(_translate("MainWindow", "fileopen"))
        self.actionFileopen.setToolTip(_translate("MainWindow", "Fileopen"))
        self.actionOpenurl.setText(_translate("MainWindow", "urlopen"))
        self.actionOpenurl.setToolTip(_translate("MainWindow", "whois.domaintools.com"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit"))
        self.pushButton.setToolTip(_translate("MainWindow", "Save"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Search"))

import dnslookup_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

