# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageViewer(object):
    def setupUi(self, ImageViewer):
        ImageViewer.setObjectName("ImageViewer")
        ImageViewer.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(ImageViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.lblPicContainer = QtWidgets.QLabel(self.centralwidget)
        self.lblPicContainer.setGeometry(QtCore.QRect(0, 0, 740, 640))
        self.lblPicContainer.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lblPicContainer.setText("")
        self.lblPicContainer.setPixmap(QtGui.QPixmap("../../Picture - HDD/Genshin SS/Screenshot 2021-04-12 204658 (2).png"))
        self.lblPicContainer.setScaledContents(False)
        self.lblPicContainer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblPicContainer.setObjectName("lblPicContainer")
        ImageViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ImageViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageViewer)
        self.statusbar.setObjectName("statusbar")
        ImageViewer.setStatusBar(self.statusbar)
        self.actionSave_as = QtWidgets.QAction(ImageViewer)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionExit = QtWidgets.QAction(ImageViewer)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(ImageViewer)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ImageViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageViewer)

    def retranslateUi(self, ImageViewer):
        _translate = QtCore.QCoreApplication.translate
        ImageViewer.setWindowTitle(_translate("ImageViewer", "MainWindow"))
        self.menuFile.setTitle(_translate("ImageViewer", "File"))
        self.actionSave_as.setText(_translate("ImageViewer", "Save as.."))
        self.actionExit.setText(_translate("ImageViewer", "Exit"))
        self.actionSave.setText(_translate("ImageViewer", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageViewer = QtWidgets.QMainWindow()
    ui = Ui_ImageViewer()
    ui.setupUi(ImageViewer)
    ImageViewer.show()
    sys.exit(app.exec_())

