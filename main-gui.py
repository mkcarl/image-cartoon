from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QFileDialog, QMessageBox, QDesktopWidget
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import cv2
import os
import numpy as np
import cartoonify

class Ui_Properties(object):
    def setupUi(self, Properties):
        Properties.setObjectName("Properties")
        Properties.resize(480, 520)
        Properties.setMinimumSize(QtCore.QSize(480, 520))
        Properties.setMaximumSize(QtCore.QSize(480, 520))
        Properties.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(Properties)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(32, 22, 136, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 69, 160, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(31, 192, 164, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(31, 277, 176, 35))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.slideFilter = QtWidgets.QSlider(self.centralwidget)
        self.slideFilter.setGeometry(QtCore.QRect(180, 321, 270, 22))
        self.slideFilter.setSizeIncrement(QtCore.QSize(3, 0))
        self.slideFilter.setOrientation(QtCore.Qt.Horizontal)
        self.slideFilter.setObjectName("slideFilter")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(51, 320, 109, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(51, 113, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(51, 150, 115, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setScaledContents(False)
        self.label_8.setObjectName("label_8")
        self.spinBlurVal = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBlurVal.setGeometry(QtCore.QRect(180, 150, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinBlurVal.setFont(font)
        self.spinBlurVal.setObjectName("spinBlurVal")
        self.spinKcluster = QtWidgets.QSpinBox(self.centralwidget)
        self.spinKcluster.setGeometry(QtCore.QRect(180, 235, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinKcluster.setFont(font)
        self.spinKcluster.setObjectName("spinKcluster")
        self.txtSigma = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSigma.setGeometry(QtCore.QRect(179, 360, 270, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txtSigma.setFont(font)
        self.txtSigma.setObjectName("txtSigma")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(270, 420, 167, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnPreview = QtWidgets.QPushButton(self.centralwidget)
        self.btnPreview.setGeometry(QtCore.QRect(50, 420, 176, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnPreview.setFont(font)
        self.btnPreview.setObjectName("btnPreview")
        self.txtImgFile = QtWidgets.QLineEdit(self.centralwidget)
        self.txtImgFile.setReadOnly(True)
        self.txtImgFile.setGeometry(QtCore.QRect(174, 23, 240, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.txtImgFile.setFont(font)
        self.txtImgFile.setObjectName("txtImgFile")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(420, 22, 31, 31))
        self.btnBrowse.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Download - HDD/opened-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBrowse.setIcon(icon)
        self.btnBrowse.setFlat(True)
        self.btnBrowse.setObjectName("btnBrowse")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 360, 135, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(51, 235, 126, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.spinLineSize = QtWidgets.QSpinBox(self.centralwidget)
        self.spinLineSize.setGeometry(QtCore.QRect(180, 110, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.spinLineSize.setFont(font)
        self.spinLineSize.setObjectName("spinLineSize")
        Properties.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Properties)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        Properties.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Properties)
        self.statusbar.setObjectName("statusbar")
        Properties.setStatusBar(self.statusbar)

        self.retranslateUi(Properties)
        self.defaultValueUi()
        self.configControlsUi()
        QtCore.QMetaObject.connectSlotsByName(Properties)

        self.btnPreview.clicked.connect(self.btnPreview_clicked)
        self.btnBrowse.clicked.connect(self.btnBrowse_clicked)
        self.btnSave.clicked.connect(self.btnSave_clicked)

    def retranslateUi(self, Properties):
        _translate = QtCore.QCoreApplication.translate
        Properties.setWindowTitle(_translate("Properties", "Properties"))
        self.label.setText(_translate("Properties", "Image file : "))
        self.label_2.setText(_translate("Properties", "Edge setting : "))
        self.label_3.setText(_translate("Properties", "Color setting : "))
        self.label_4.setText(_translate("Properties", "Noise filtering : "))
        self.label_5.setText(_translate("Properties", "Filter size : "))
        self.label_7.setText(_translate("Properties", "Line size : "))
        self.label_8.setText(_translate("Properties", "Blur value : "))
        self.btnSave.setText(_translate("Properties", "Save image"))
        self.btnPreview.setText(_translate("Properties", "Generate Preview"))
        self.label_9.setText(_translate("Properties", "Sigma value : "))
        self.label_6.setText(_translate("Properties", "K - clusters : "))

    def defaultValueUi(self):
        self.spinLineSize.setValue(7)
        self.spinBlurVal.setValue(7)
        self.spinKcluster.setValue(9)
        self.slideFilter.setValue(3)
        self.txtSigma.setText("200")

    def configControlsUi(self):
        self.spinLineSize.lineEdit().setReadOnly(True)
        self.spinLineSize.setRange(3, 99)
        self.spinLineSize.setSingleStep(2)
        self.spinBlurVal.lineEdit().setReadOnly(True)
        self.spinBlurVal.setRange(1, 99)
        self.spinBlurVal.setSingleStep(2)
        self.spinKcluster.lineEdit().setReadOnly(True)
        self.spinKcluster.setRange(3, 29)
        self.spinKcluster.setSingleStep(2)
        self.slideFilter.setRange(1, 8)
        self.slideFilter.setTickInterval(1)
        self.slideFilter.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slideFilter.valueChanged.connect(lambda x: self.slideFilter.setToolTip(str(self.slideFilter.value()*2-1)))
        self.slideFilter.setToolTip(str(self.slideFilter.value()))

    def toggleAllControl(self, flag:bool):
        self.centralwidget.setEnabled(flag)
        # controls = (self.centralwidget.layout().itemAt(i) for i in range(self.centralwidget.layout().count()))
        # for control in controls:
        #     pass

    def worker_finished(self, img):
        self.toggleAllControl(True)
        self.ImgPreviewWindow = QtWidgets.QMainWindow()
        ui = Ui_ImageViewer()
        ui.setupUi(self.ImgPreviewWindow)
        ui.showImage(self.ImgPreviewWindow, img)
        ui.actionExit.triggered.connect(lambda:self.ImgPreviewWindow.close())
        self.ImgPreviewWindow.show()

    def saveImg(self, img):
        if not os.path.exists("./output"):
            os.mkdir("./output")
        name, _ = QFileDialog.getSaveFileName(self.centralwidget, "Save as..", "./output/")
        if name != "":
            cv2.imwrite(f"{name}.png", img)
        self.toggleAllControl(True)

    def btnPreview_clicked(self):
        self.toggleAllControl(False)
        img = cv2.imread(self.txtImgFile.text())
        if img is not None:
            self.worker = CartoonWorker(
                img, int(self.spinLineSize.value()), int(self.spinBlurVal.value()), int(self.spinKcluster.value()),
                int(self.slideFilter.value()*2-1), int(self.txtSigma.text())
            )
            self.worker.start()
            self.worker.returnImg.connect(self.worker_finished)
        else:
            QMessageBox.critical(self.centralwidget, "Error", "Please choose a valid image file.", QMessageBox.Ok)
            self.toggleAllControl(True)

    def btnSave_clicked(self):
        self.toggleAllControl(False)
        img = cv2.imread(self.txtImgFile.text())
        if img is not None:
            self.worker = CartoonWorker(
                img, int(self.spinLineSize.value()), int(self.spinBlurVal.value()), int(self.spinKcluster.value()),
                int(self.slideFilter.value() * 2 - 1), int(self.txtSigma.text())
            )
            self.worker.start()
            self.worker.returnImg.connect(self.saveImg)
        else:
            QMessageBox.critical(self.centralwidget, "Error", "Please choose a valid image file.", QMessageBox.Ok)
            self.toggleAllControl(True)

    def btnBrowse_clicked(self):
        filedir = QFileDialog.getOpenFileName(caption="Open", directory="./input",filter="Images (*.png *.xpm *.jpg *.jpeg *.tiff *.gif)")
        self.txtImgFile.setText(filedir[0])


class CartoonWorker(QThread):
    returnImg = pyqtSignal(np.ndarray)
    def __init__(self, img, line, blur, kcluster, filter, sigma, parent=None):
        QThread.__init__(self, parent=parent)
        self.line = line
        self.blur = blur
        self.kcluster = kcluster
        self.filter = filter
        self.sigma = sigma
        self.img = img

    def run(self):
        img2 = cartoonify.edge_mask(self.img, int(self.line), int(self.blur))
        img3 = cartoonify.color_quantization(self.img, self.kcluster)
        img4 = cartoonify.blur_img(img3, self.filter, self.sigma, self.sigma)
        img5 = cartoonify.combine(img2, img4)
        self.returnImg.emit(img5)


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
        self.actionExit = QtWidgets.QAction(ImageViewer)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Esc")
        self.actionSave = QtWidgets.QAction(ImageViewer)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.actionSave.triggered.connect(lambda: self.actionSave_clicked())

        self.retranslateUi(ImageViewer)
        QtCore.QMetaObject.connectSlotsByName(ImageViewer)

    def retranslateUi(self, ImageViewer):
        _translate = QtCore.QCoreApplication.translate
        ImageViewer.setWindowTitle(_translate("ImageViewer", "ImageViewer"))
        self.menuFile.setTitle(_translate("ImageViewer", "File"))
        self.actionExit.setText(_translate("ImageViewer", "Exit"))
        self.actionSave.setText(_translate("ImageViewer", "Save"))

        qtRectangle = ImageViewer.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        ImageViewer.move(qtRectangle.topLeft())


    def showImage(self, ImageViewer, fileName:str):
        img = cv2.imread(fileName)
        height, width, channels = img.shape
        qImg = QtGui.QImage(img.data, width, height, channels*width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.lblPicContainer.setPixmap(QtGui.QPixmap(pixmap))
        self.lblPicContainer.resize(width, height)
        ImageViewer.resize(width, height)

    def showImage(self, ImageViewer, image:np.ndarray):
        height, width, channels = image.shape
        qImg = QtGui.QImage(image.data, width, height, channels*width, QtGui.QImage.Format_BGR888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.lblPicContainer.setPixmap(QtGui.QPixmap(pixmap))
        self.lblPicContainer.resize(width, height)
        ImageViewer.resize(width, height)
        ImageViewer.setFixedSize(width, height)


    def actionSave_clicked(self):
        if not os.path.exists("./output"):
            os.mkdir("./output")
        name, _ = QFileDialog.getSaveFileName(self.centralwidget, "Save as..", "./output/")
        if name != "":
            self.lblPicContainer.pixmap().save(f"{name}.png", format="PNG")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    ui = Ui_Properties()
    ui.setupUi(main)
    main.show()
    sys.exit(app.exec_())
