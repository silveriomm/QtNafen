# -*- coding: utf-8 -*-

import os.path
import ConfigParser
config = ConfigParser.ConfigParser()

config.read(".qtnafen.cfg")

dir_snes = config.get("ROMPATH", "SNES")
dir_gen = config.get("ROMPATH", "GEN")
dir_nes = config.get("ROMPATH", "NES")
dir_sms = config.get("ROMPATH", "SMS")
dir_psx = config.get("ROMPATH", "PSX")
dir_sat = config.get("ROMPATH", "SAT")

comando_snes = config.get("COMMAND_PATH", "SNES_RUN")
comando_gens = config.get("COMMAND_PATH", "GEN_RUN")
comando_nes = config.get("COMMAND_PATH", "NES_RUN")
comando_sms = config.get("COMMAND_PATH", "SMS_RUN")
comando_psx = config.get("COMMAND_PATH", "PSX_RUN")
comando_sat = config.get("COMMAND_PATH", "SAT_RUN")

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(500, 224)
        Dialog.setMinimumSize(QtCore.QSize(500, 224))
        Dialog.setMaximumSize(QtCore.QSize(500, 224))
        self.btAceitar = QtGui.QPushButton(Dialog)
        self.btAceitar.setGeometry(QtCore.QRect(410, 190, 75, 23))
        self.btAceitar.setObjectName("btAceitar")
        self.btCancelar = QtGui.QPushButton(Dialog)
        self.btCancelar.setGeometry(QtCore.QRect(330, 190, 75, 23))
        self.btCancelar.setObjectName("btCancelar")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 170))
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edSnes = QtGui.QLineEdit(self.widget)
        self.edSnes.setObjectName("edSnes")
        self.edSnes.setText(dir_snes)
        self.gridLayout.addWidget(self.edSnes, 0, 1, 1, 1)
        self.btSnes = QtGui.QPushButton(self.widget)
        self.btSnes.setObjectName("btSnes")
        self.gridLayout.addWidget(self.btSnes, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.edGenesis = QtGui.QLineEdit(self.widget)
        self.edGenesis.setObjectName("edGenesis")
        self.edGenesis.setText(dir_gen)
        self.gridLayout.addWidget(self.edGenesis, 1, 1, 1, 1)
        self.btGenesis = QtGui.QPushButton(self.widget)
        self.btGenesis.setObjectName("btGenesis")
        self.gridLayout.addWidget(self.btGenesis, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.edNes = QtGui.QLineEdit(self.widget)
        self.edNes.setObjectName("edNes")
        self.edNes.setText(dir_nes)
        self.gridLayout.addWidget(self.edNes, 2, 1, 1, 1)
        self.btNes = QtGui.QPushButton(self.widget)
        self.btNes.setObjectName("btNes")
        self.gridLayout.addWidget(self.btNes, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.edSms = QtGui.QLineEdit(self.widget)
        self.edSms.setObjectName("edSms")
        self.edSms.setText(dir_sms)
        self.gridLayout.addWidget(self.edSms, 3, 1, 1, 1)
        self.btSms = QtGui.QPushButton(self.widget)
        self.btSms.setObjectName("btSms")
        self.gridLayout.addWidget(self.btSms, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.edPsx = QtGui.QLineEdit(self.widget)
        self.edPsx.setObjectName("edPsx")
        self.edPsx.setText(dir_psx)
        self.gridLayout.addWidget(self.edPsx, 4, 1, 1, 1)
        self.btPsx = QtGui.QPushButton(self.widget)
        self.btPsx.setObjectName("btPsx")
        self.gridLayout.addWidget(self.btPsx, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.edSaturn = QtGui.QLineEdit(self.widget)
        self.edSaturn.setObjectName("edSaturn")
        self.edSaturn.setText(dir_sat)
        self.gridLayout.addWidget(self.edSaturn, 5, 1, 1, 1)
        self.btSaturn = QtGui.QPushButton(self.widget)
        self.btSaturn.setObjectName("btSaturn")
        self.gridLayout.addWidget(self.btSaturn, 5, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.btSnes, QtCore.SIGNAL("clicked()"), self.openSnes)
        QtCore.QObject.connect(self.btGenesis, QtCore.SIGNAL("clicked()"), self.openGenesis)
        QtCore.QObject.connect(self.btNes, QtCore.SIGNAL("clicked()"), self.openNes)
        QtCore.QObject.connect(self.btSms, QtCore.SIGNAL("clicked()"), self.openSms)
        QtCore.QObject.connect(self.btPsx, QtCore.SIGNAL("clicked()"), self.openPsx)
        QtCore.QObject.connect(self.btSaturn, QtCore.SIGNAL("clicked()"), self.openSaturn)
        QtCore.QObject.connect(self.btAceitar, QtCore.SIGNAL("clicked()"), self.aplicar)
        QtCore.QObject.connect(self.btCancelar, QtCore.SIGNAL("clicked()"), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btAceitar.setText(QtGui.QApplication.translate("Dialog", "Aceitar", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "SNES", None, QtGui.QApplication.UnicodeUTF8))
        self.btSnes.setText(QtGui.QApplication.translate("Dialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "GENENSIS", None, QtGui.QApplication.UnicodeUTF8))
        self.btGenesis.setText(QtGui.QApplication.translate("Dialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "NES", None, QtGui.QApplication.UnicodeUTF8))
        self.btNes.setText(QtGui.QApplication.translate("Dialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "SMS", None, QtGui.QApplication.UnicodeUTF8))
        self.btSms.setText(QtGui.QApplication.translate("Dialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "PSX", None, QtGui.QApplication.UnicodeUTF8))
        self.btPsx.setText(QtGui.QApplication.translate("Dialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "SATURN", None, QtGui.QApplication.UnicodeUTF8))
        self.btSaturn.setText(QtGui.QApplication.translate("Dialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))

    def openSnes(self):
        global dir_snes
        dir_snes = QtGui.QFileDialog.getExistingDirectory()
        self.edSnes.setText(dir_snes)

    def openGenesis(self):
        global dir_gen
        dir_gen = QtGui.QFileDialog.getExistingDirectory()
        self.edGenesis.setText(dir_gen)

    def openNes(self):
        global dir_nes
        dir_nes = QtGui.QFileDialog.getExistingDirectory()
        self.edNes.setText(dir_nes)

    def openSms(self):
        global dir_sms
        dir_sms = QtGui.QFileDialog.getExistingDirectory()
        self.edSms.setText(dir_sms)

    def openPsx(self):
        global dir_psx
        dir_psx = QtGui.QFileDialog.getExistingDirectory()
        self.edPsx.setText(dir_psx)

    def openSaturn(self):
        global dir_sat
        dir_sat = QtGui.QFileDialog.getExistingDirectory()
        self.edSaturn.setText(dir_sat)

    def aplicar(self):
        global dir_snes
        global dir_gen
        global dir_nes
        global dir_sms
        global dir_psx
        global dir_sat
        dir_snes = self.edSnes.text()
        dir_gen = self.edGenesis.text()
        dir_nes = self.edNes.text()
        dir_sms = self.edSms.text()
        dir_psx = self.edPsx.text()
        dir_sat = self.edSaturn.text()
        config.set("ROMPATH", "SNES", dir_snes)
        config.set("ROMPATH", "GEN", dir_gen)
        config.set("ROMPATH", "NES", dir_nes)
        config.set("ROMPATH", "SMS", dir_sms)
        config.set("ROMPATH", "PSX", dir_psx)
        config.set("ROMPATH", "SAT", dir_sat)
        arquivo_cfg = open(".qtnafen.cfg", "w")
        config.write(arquivo_cfg)
        arquivo_cfg.close()
        Dialog.close()
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

