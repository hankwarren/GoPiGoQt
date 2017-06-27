#!/usr/bin/python

import sip
sip.setapi('QString', 1)
import sys
import os
import bluetooth
#import socket

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication


form_class = uic.loadUiType('gopigo.ui')[0]
bt_addr = '00:1A:7D:DA:71:13'
bt_port = 1

GOPIGO = '10.0.0.103'
PORT = 8000

class GoPiGo(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.backwardButton.clicked.connect(self.backwardClick)
        self.forwardButton.clicked.connect(self.forwardClick)
        self.stopButton.clicked.connect(self.stopClick)
        self.leftButton.clicked.connect(self.leftClick)
        self.rightButton.clicked.connect(self.rightClick)
        self.rotateLeftButton.clicked.connect(self.rotateLeftClick)
        self.rotateRightButton.clicked.connect(self.rotateRightClick)
        self.sLeftButton.clicked.connect(self.sLeftClick)
        self.sRightButton.clicked.connect(self.sRightClick)
        self.homeButton.clicked.connect(self.homeClick)

        #self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((bt_addr, bt_port))

    def backwardClick(self):
        self.write('backward')

    def forwardClick(self):
        self.write('forward')

    def stopClick(self):
        self.write('stop')

    def leftClick(self):
        self.write('left')

    def rightClick(self):
        self.write('right')

    def rotateLeftClick(self):
        self.write('rotl')

    def rotateRightClick(self):
        self.write('rotr')

    def sLeftClick(self):
        self.write('sleft')

    def sRightClick(self):
        self.write('sright')

    def homeClick(self):
        self.write('home')

    def write(self, command):
        self.sock.send(command)
        data = self.sock.recv(1024)
        print('data: ' + data)

        #self.sock.sendto(command, (GOPIGO, PORT))
        #self.sock.recv(1024)

def main():
    app = QApplication(sys.argv)
    mainWindow = GoPiGo()
    mainWindow.show()
    sys.exit(app.exec_())
    mainWindow.sock.close()

if __name__ == '__main__':
    main()

