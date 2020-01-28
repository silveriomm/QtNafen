# -*- coding: utf-8 -*-

import os, fnmatch
import os.path
import ConfigParser
from _socket import IP_RECVDSTADDR
from PySide.QtGui import QMessageBox
config = ConfigParser.ConfigParser()

from PySide import QtCore, QtGui

try:
    arquivo_cfg = open(".qtnafen.cfg", "r+")
except:
    arquivo_cfg = open(".qtnafen.cfg", "w")
    arquivo_cfg.write("[EMUL]\n")
    arquivo_cfg.write("EMU = \n")
    arquivo_cfg.write("[ROMPATH]\n")
    arquivo_cfg.write("SNES = \n")
    arquivo_cfg.write("GEN = \n")
    arquivo_cfg.write("NES = \n")
    arquivo_cfg.write("SMS = \n")
    arquivo_cfg.write("PSX = \n")
    arquivo_cfg.write("SAT= \n")
    arquivo_cfg.write("[COMMAND_PATH]\n")
    arquivo_cfg.write("SNES_RUN = mednafen --sound.driver default "+
                                          "--sound.device default "+
                                          "--sound.rate 48000 "+
                                          "--video.driver opengl "+
                                          "--snes.pixshader none "+
                                          "--snes.videoip 1 "+
                                          "--video.glvsync 0 "+
                                          "--video.blit_timesync 0 "+
                                          "--snes.stretch 1 --video.fs 1\n")
    arquivo_cfg.write("GEN_RUN = mednafen --sound.driver default "+
                                          "--sound.device default "+
                                          "--sound.rate 48000 "+
                                          "--video.driver opengl "+
                                          "--md.pixshader none "+
                                          "--md.videoip 1 "+
                                          "--video.glvsync 0 "+
                                          "--video.blit_timesync 0 "+
                                          "--md.stretch 1 "+
                                          "--video.fs 1\n")
    arquivo_cfg.write("NES_RUN = mednafen --sound.driver default "+
                                          "--sound.device default "+
                                          "--sound.rate 48000 "+
                                          "--video.driver opengl "+
                                          "--nes.pixshader none "+
                                          "--nes.videoip 1 "+
                                          "--video.glvsync 0 "+
                                          "--video.blit_timesync 0 "+
                                          "--nes.stretch 1 "+
                                          "--video.fs 1\n")
    arquivo_cfg.write("SMS_RUN = mednafen --sound.driver default "+
                                          "--sound.device default "+
                                          "--sound.rate 48000 "+
                                          "--video.driver opengl "+
                                          "--sms.pixshader none "+
                                          "--sms.videoip 1 "+
                                          "--video.glvsync 0 "+
                                          "--video.blit_timesync 0 "+
                                          "--sms.stretch 1 "+
                                          "--video.fs 1\n")
    arquivo_cfg.write("PSX_RUN = mednafen --sound.driver default "+
                                         "--sound.device default "+
                                         "--sound.rate 48000 "+
                                         "--psx.spu.resamp_quality 0 "+
                                         "--video.driver opengl "+
                                         "--video.glvsync 0 "+
                                         "--video.blit_timesync 0 "+
                                         "--psx.pixshader none "+
                                         "--psx.videoip 1 --psx.stretch 1 "+
                                         "--video.fs 1\n")
    arquivo_cfg.write("SAT_RUN = mednafen --sound.driver default "+
                                         "--sound.device default "+
                                         "--sound.rate 48000 "+
                                         "--video.driver opengl "+
                                         "--video.glvsync 0 "+
                                         "--video.blit_timesync 0 "+
                                         "--ss.scsp.resamp_quality 4 "+
                                         "--ss.stretch 1 "+
                                         "--ss.videoip 1 "
                                         "--video.fs 1\n")
    arquivo_cfg.close()
    arquivo_cfg = open(".qtnafen.cfg", "r+")

config.read(".qtnafen.cfg")

emu = config.get("EMUL", "EMU")

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

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName("ConfigDialog")
        ConfigDialog.resize(494, 253)
        self.label = QtGui.QLabel(ConfigDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(ConfigDialog)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(ConfigDialog)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(ConfigDialog)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 111, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(ConfigDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_5.setObjectName("label_5")
        self.cbGlvsync = QtGui.QCheckBox(ConfigDialog)
        self.cbGlvsync.setGeometry(QtCore.QRect(10, 120, 121, 17))
        self.cbGlvsync.setChecked(True)
        self.cbGlvsync.setObjectName("cbGlvsync")
        self.cbTimesync = QtGui.QCheckBox(ConfigDialog)
        self.cbTimesync.setGeometry(QtCore.QRect(10, 140, 121, 17))
        self.cbTimesync.setChecked(True)
        self.cbTimesync.setObjectName("cbTimesync")
        self.label_6 = QtGui.QLabel(ConfigDialog)
        self.label_6.setGeometry(QtCore.QRect(230, 10, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(ConfigDialog)
        self.label_7.setGeometry(QtCore.QRect(140, 60, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(ConfigDialog)
        self.label_8.setGeometry(QtCore.QRect(270, 60, 61, 16))
        self.label_8.setObjectName("label_8")
        self.cbBilinear = QtGui.QCheckBox(ConfigDialog)
        self.cbBilinear.setGeometry(QtCore.QRect(140, 120, 81, 17))
        self.cbBilinear.setChecked(True)
        self.cbBilinear.setObjectName("cbBilinear")
        self.cbFullScreen = QtGui.QCheckBox(ConfigDialog)
        self.cbFullScreen.setGeometry(QtCore.QRect(140, 140, 70, 17))
        self.cbFullScreen.setChecked(True)
        self.cbFullScreen.setObjectName("cbFullScreen")
        self.label_9 = QtGui.QLabel(ConfigDialog)
        self.label_9.setGeometry(QtCore.QRect(390, 60, 81, 16))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtGui.QWidget(ConfigDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 120, 50, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.cmbYscale = QtGui.QComboBox(self.layoutWidget)
        self.cmbYscale.setObjectName("cmbYscale")
        self.cmbYscale.addItem("")
        self.cmbYscale.addItem("")
        self.cmbYscale.addItem("")
        self.cmbYscale.addItem("")
        self.cmbYscale.addItem("")
        self.cmbYscale.addItem("")
        self.cmbYscale.addItem("")
        self.verticalLayout_2.addWidget(self.cmbYscale)
        self.layoutWidget_2 = QtGui.QWidget(ConfigDialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(360, 120, 50, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtGui.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.cmbXscaleFS = QtGui.QComboBox(self.layoutWidget_2)
        self.cmbXscaleFS.setObjectName("cmbXscaleFS")
        self.cmbXscaleFS.addItem("")
        self.cmbXscaleFS.addItem("")
        self.cmbXscaleFS.addItem("")
        self.cmbXscaleFS.addItem("")
        self.cmbXscaleFS.addItem("")
        self.cmbXscaleFS.addItem("")
        self.cmbXscaleFS.addItem("")
        self.verticalLayout_3.addWidget(self.cmbXscaleFS)
        self.layoutWidget_3 = QtGui.QWidget(ConfigDialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(430, 120, 50, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtGui.QLabel(self.layoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.cmbYscaleFS = QtGui.QComboBox(self.layoutWidget_3)
        self.cmbYscaleFS.setObjectName("cmbYscaleFS")
        self.cmbYscaleFS.addItem("")
        self.cmbYscaleFS.addItem("")
        self.cmbYscaleFS.addItem("")
        self.cmbYscaleFS.addItem("")
        self.cmbYscaleFS.addItem("")
        self.cmbYscaleFS.addItem("")
        self.cmbYscaleFS.addItem("")
        self.verticalLayout_4.addWidget(self.cmbYscaleFS)
        self.label_14 = QtGui.QLabel(ConfigDialog)
        self.label_14.setGeometry(QtCore.QRect(10, 170, 211, 16))
        self.label_14.setObjectName("label_14")
        self.layoutWidget1 = QtGui.QWidget(ConfigDialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 120, 50, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtGui.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.cmbXscale = QtGui.QComboBox(self.layoutWidget1)
        self.cmbXscale.setObjectName("cmbXscale")
        self.cmbXscale.addItem("")
        self.cmbXscale.addItem("")
        self.cmbXscale.addItem("")
        self.cmbXscale.addItem("")
        self.cmbXscale.addItem("")
        self.cmbXscale.addItem("")
        self.cmbXscale.addItem("")
        self.verticalLayout.addWidget(self.cmbXscale)
        self.btAceitar = QtGui.QPushButton(ConfigDialog)
        self.btAceitar.setGeometry(QtCore.QRect(410, 220, 71, 23))
        self.btAceitar.setMinimumSize(QtCore.QSize(71, 23))
        self.btAceitar.setMaximumSize(QtCore.QSize(71, 16777215))
        self.btAceitar.setObjectName("btAceitar")
        self.btCancelar = QtGui.QPushButton(ConfigDialog)
        self.btCancelar.setGeometry(QtCore.QRect(320, 220, 75, 23))
        self.btCancelar.setMinimumSize(QtCore.QSize(75, 23))
        self.btCancelar.setMaximumSize(QtCore.QSize(75, 16777215))
        self.btCancelar.setObjectName("btCancelar")
        self.layoutWidget2 = QtGui.QWidget(ConfigDialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 190, 471, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edMednafen = QtGui.QLineEdit(self.layoutWidget2)
        self.edMednafen.setObjectName("edMednafen")
        self.horizontalLayout.addWidget(self.edMednafen)
        self.btBuscar = QtGui.QPushButton(self.layoutWidget2)
        self.btBuscar.setObjectName("btBuscar")
        self.horizontalLayout.addWidget(self.btBuscar)
        self.layoutWidget3 = QtGui.QWidget(ConfigDialog)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 441, 24))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cmbAudioDriver = QtGui.QComboBox(self.layoutWidget3)
        self.cmbAudioDriver.setObjectName("cmbAudioDriver")
        self.cmbAudioDriver.addItem("")
        self.cmbAudioDriver.addItem("")
        self.cmbAudioDriver.addItem("")
        self.cmbAudioDriver.addItem("")
        self.cmbAudioDriver.addItem("")
        self.cmbAudioDriver.addItem("")
        self.cmbAudioDriver.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbAudioDriver)
        self.cmbAudioDevice = QtGui.QComboBox(self.layoutWidget3)
        self.cmbAudioDevice.setObjectName("cmbAudioDevice")
        self.cmbAudioDevice.addItem("")
        self.cmbAudioDevice.addItem("")
        self.cmbAudioDevice.addItem("")
        self.cmbAudioDevice.addItem("")
        self.cmbAudioDevice.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbAudioDevice)
        self.cmbAudioRate = QtGui.QComboBox(self.layoutWidget3)
        self.cmbAudioRate.setObjectName("cmbAudioRate")
        self.cmbAudioRate.addItem("")
        self.cmbAudioRate.addItem("")
        self.cmbAudioRate.addItem("")
        self.cmbAudioRate.addItem("")
        self.cmbAudioRate.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbAudioRate)
        self.cmbResolution = QtGui.QComboBox(self.layoutWidget3)
        self.cmbResolution.setObjectName("cmbResolution")
        self.cmbResolution.addItem("")
        self.cmbResolution.addItem("")
        self.cmbResolution.addItem("")
        self.cmbResolution.addItem("")
        self.cmbResolution.addItem("")
        self.horizontalLayout_2.addWidget(self.cmbResolution)
        self.sldSPUresample = QtGui.QSlider(self.layoutWidget3)
        self.sldSPUresample.setMaximum(10)
        self.sldSPUresample.setOrientation(QtCore.Qt.Horizontal)
        self.sldSPUresample.setObjectName("sldSPUresample")
        self.horizontalLayout_2.addWidget(self.sldSPUresample)
        self.layoutWidget4 = QtGui.QWidget(ConfigDialog)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 80, 471, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cmbVideoDriver = QtGui.QComboBox(self.layoutWidget4)
        self.cmbVideoDriver.setObjectName("cmbVideoDriver")
        self.cmbVideoDriver.addItem("")
        self.cmbVideoDriver.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbVideoDriver)
        self.cmbVideoPix = QtGui.QComboBox(self.layoutWidget4)
        self.cmbVideoPix.setObjectName("cmbVideoPix")
        self.cmbVideoPix.addItem("")
        self.cmbVideoPix.addItem("")
        self.cmbVideoPix.addItem("")
        self.cmbVideoPix.addItem("")
        self.cmbVideoPix.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbVideoPix)
        self.cmbAspect = QtGui.QComboBox(self.layoutWidget4)
        self.cmbAspect.setObjectName("cmbAspect")
        self.cmbAspect.addItem("")
        self.cmbAspect.addItem("")
        self.cmbAspect.addItem("")
        self.cmbAspect.addItem("")
        self.cmbAspect.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbAspect)
        self.cmbVideoSpecial = QtGui.QComboBox(self.layoutWidget4)
        self.cmbVideoSpecial.setObjectName("cmbVideoSpecial")
        self.cmbVideoSpecial.addItem("")
        self.cmbVideoSpecial.addItem("")
        self.cmbVideoSpecial.addItem("")
        self.cmbVideoSpecial.addItem("")
        self.cmbVideoSpecial.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbVideoSpecial)
        self.lbSPUvalue = QtGui.QLabel(ConfigDialog)
        self.lbSPUvalue.setGeometry(QtCore.QRect(460, 30, 21, 21))
        self.lbSPUvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSPUvalue.setObjectName("lbSPUvalue")

        self.retranslateUi(ConfigDialog)
        self.cmbYscale.setCurrentIndex(3)
        self.cmbXscaleFS.setCurrentIndex(3)
        self.cmbYscaleFS.setCurrentIndex(3)
        self.cmbXscale.setCurrentIndex(3)
        self.cmbAudioDriver.setCurrentIndex(1)
        self.cmbAudioDevice.setCurrentIndex(2)
        self.cmbAudioRate.setCurrentIndex(2)
        self.cmbVideoDriver.setCurrentIndex(1)
        self.cmbVideoSpecial.setCurrentIndex(1)
        QtCore.QObject.connect(self.btAceitar, QtCore.SIGNAL("clicked()"), self.aplicar)
        QtCore.QObject.connect(self.btBuscar, QtCore.SIGNAL("clicked()"), self.openEmu)
        QtCore.QObject.connect(self.btCancelar, QtCore.SIGNAL("clicked()"), self.fechar)
        QtCore.QObject.connect(self.cbBilinear, QtCore.SIGNAL("stateChanged(int)"), self.bilinear)
        QtCore.QObject.connect(self.cbFullScreen, QtCore.SIGNAL("stateChanged(int)"), self.video_fs)
        QtCore.QObject.connect(self.cbGlvsync, QtCore.SIGNAL("stateChanged(int)"), self.videosync)
        QtCore.QObject.connect(self.cbTimesync, QtCore.SIGNAL("stateChanged(int)"), self.timesync)
        QtCore.QObject.connect(self.cmbAspect, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videostretch)
        QtCore.QObject.connect(self.cmbAudioDevice, QtCore.SIGNAL("currentIndexChanged(QString)"), self.sounddevice)
        QtCore.QObject.connect(self.cmbAudioDriver, QtCore.SIGNAL("currentIndexChanged(QString)"), self.sounddriver)
        QtCore.QObject.connect(self.cmbAudioRate, QtCore.SIGNAL("currentIndexChanged(QString)"), self.soundrate)
        QtCore.QObject.connect(self.cmbResolution, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videores)
        QtCore.QObject.connect(self.cmbVideoDriver, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videodriver)
        QtCore.QObject.connect(self.cmbVideoPix, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videopix)
        QtCore.QObject.connect(self.cmbVideoSpecial, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videospecial)
        QtCore.QObject.connect(self.cmbXscale, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videoxscale)
        QtCore.QObject.connect(self.cmbXscaleFS, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videoxscaleFS)
        QtCore.QObject.connect(self.cmbYscale, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videoyscale)
        QtCore.QObject.connect(self.cmbYscaleFS, QtCore.SIGNAL("currentIndexChanged(QString)"), self.videoyscaleFS)
        QtCore.QObject.connect(self.sldSPUresample, QtCore.SIGNAL("valueChanged(int)"), self.spuresample)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(QtGui.QApplication.translate("ConfigDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigDialog", "Driver de áudio", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ConfigDialog", "Áudio device", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConfigDialog", "Áudio rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ConfigDialog", "SPU Resample Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ConfigDialog", "Vídeo driver", None, QtGui.QApplication.UnicodeUTF8))
        self.cbGlvsync.setText(QtGui.QApplication.translate("ConfigDialog", "Desabilitar Glvsync", None, QtGui.QApplication.UnicodeUTF8))
        self.cbTimesync.setText(QtGui.QApplication.translate("ConfigDialog", "Desabilitar Timesync", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ConfigDialog", "Resolução", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ConfigDialog", "Vídeo PixShader", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ConfigDialog", "Aspecto", None, QtGui.QApplication.UnicodeUTF8))
        self.cbBilinear.setText(QtGui.QApplication.translate("ConfigDialog", "Filtro bilinear", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFullScreen.setText(QtGui.QApplication.translate("ConfigDialog", "Tela Cheia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ConfigDialog", "Vídeo Special", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ConfigDialog", "Yscale", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "0.20", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "0.40", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "0.60", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "0.80", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(5, QtGui.QApplication.translate("ConfigDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscale.setItemText(6, QtGui.QApplication.translate("ConfigDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ConfigDialog", "XscaleFS", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "0.20", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "0.40", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "0.60", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "0.80", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(5, QtGui.QApplication.translate("ConfigDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscaleFS.setItemText(6, QtGui.QApplication.translate("ConfigDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ConfigDialog", "YscaleFS", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "0.20", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "0.40", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "0.60", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "0.80", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(5, QtGui.QApplication.translate("ConfigDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbYscaleFS.setItemText(6, QtGui.QApplication.translate("ConfigDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ConfigDialog", "Caminho do executável do mednafen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ConfigDialog", "Xscale", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "0.20", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "0.40", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "0.60", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "0.80", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(5, QtGui.QApplication.translate("ConfigDialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbXscale.setItemText(6, QtGui.QApplication.translate("ConfigDialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.btAceitar.setText(QtGui.QApplication.translate("ConfigDialog", "Aceitar", None, QtGui.QApplication.UnicodeUTF8))
        self.btCancelar.setText(QtGui.QApplication.translate("ConfigDialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btBuscar.setText(QtGui.QApplication.translate("ConfigDialog", "Buscar...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "SDL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "Alsa", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "Jack", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "Dsound", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(5, QtGui.QApplication.translate("ConfigDialog", "Wasapi", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDriver.setItemText(6, QtGui.QApplication.translate("ConfigDialog", "Wasapish", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDevice.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "SDL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDevice.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "Alsa", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDevice.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDevice.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "Sexyal", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioDevice.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "Pulse", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioRate.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "22050", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioRate.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "44100", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioRate.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "48000", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioRate.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "96000", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAudioRate.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "192000", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbResolution.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "640x480", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbResolution.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "800x600", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbResolution.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "960x720", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbResolution.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "1024x768", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbResolution.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "1366x768", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoDriver.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "SDL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoDriver.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "OpenGL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoPix.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoPix.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "Autoip", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoPix.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "Autoip Sharper", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoPix.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "IpSharper", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoPix.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "SABR", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAspect.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "Aspect Full", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAspect.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "Aspect Int", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAspect.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "Aspect", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAspect.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "Aspect Mult2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbAspect.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "Aspect 0", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoSpecial.setItemText(0, QtGui.QApplication.translate("ConfigDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoSpecial.setItemText(1, QtGui.QApplication.translate("ConfigDialog", "2xsai", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoSpecial.setItemText(2, QtGui.QApplication.translate("ConfigDialog", "Super2xsai", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoSpecial.setItemText(3, QtGui.QApplication.translate("ConfigDialog", "Supereagle", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbVideoSpecial.setItemText(4, QtGui.QApplication.translate("ConfigDialog", "Hq2x", None, QtGui.QApplication.UnicodeUTF8))
        self.lbSPUvalue.setText(QtGui.QApplication.translate("ConfigDialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.edMednafen.setText(emu)

    def fechar(self):
        ConfigDialog.close()

    def openEmu(self):
        global emu
        emu = QtGui.QFileDialog.getOpenFileName(None, "Abrir arquivo executável", "~/",
                                                    "Arquivo .exe (*.exe)")
        self.edMednafen.setText(str(emu[0]))

    def bilinear(self):
        global video_bilinear
        if self.cbBilinear.isChecked():
            video_bilinear = '.videoip 1'
        else:
            video_bilinear = '.videoip 0'
        
    def videosync(self):
        global video_sync
        if self.cbGlvsync.isChecked():
            video_sync = '--video.glvsync 0'
        else:
            video_sync = '--video.glvsync 1'
            
    def timesync(self):
        global time_sync
        if self.cbTimesync.isChecked():
            time_sync = '--video.blit_timesync 0'
        else:
            time_sync = '--video.blit_timesync 1'
            
    def video_fs(self):
        global videofs
        if self.cbFullScreen.isChecked():
            videofs = '--video.fs 1'
        else:
            videofs = '--video.fs 0'
            
    def sounddriver(self):
        global sound_driver
        global sd
        sd = self.cmbAudioDriver.currentText()
        if sd == 'SDL':
            sound_driver = '--sound.driver sdl'
        elif sd == 'Default':
            sound_driver = '--sound.driver default'
        elif sd == 'Alsa':
            sound_driver = '--sound.driver alsa'
        elif sd == 'Jack':
            sound_driver = '--sound.driver jack'
        elif sd == 'Dsound':
            sound_driver = '--sound.driver dsound'
        elif sd == 'Wasapi':
            sound_driver = '--sound.driver wasapi'
        elif sd == 'Wasapish':
            sound_driver = '--sound.driver wasapish'
            
    def sounddevice(self):
        global sound_device
        global sdv
        sdv = self.cmbAudioDevice.currentText()    
        if sdv == 'SLD':
            sound_device = '--sound.device sdl'
        elif sdv == 'Alsa':
            sound_device = '--sound.device alsa'
        elif sdv == 'Default':
            sound_device = '--sound.device default'
        elif sdv == 'Sexyal':
            sound_device = '--sound.device sexyal-literal-default'
        elif sdv == 'Pulse':
            sound_device = '--sound.device pulse'
            
    def soundrate(self):
        global sound_rate
        global sr
        sr = self.cmbAudioRate.currentText()
        if sr == '22050':
            sound_rate = '--sound.rate 22050'
        elif sr == '44100':
            sound_rate = '--sound.rate 44100'
        elif sr == '48000':
            sound_rate = '--sound.rate 48000'
        elif sr == '96000':
            sound_rate = '--sound.rate 96000'
        elif sr == '192000':
            sound_rate = '--sound.rate 192000'
            
    def videores(self):
        global video_xres
        global video_yres
        global vr
        vr = self.cmbResolution.currentText()
        if vr == '640x480':
            video_xres = '.xres 640'
            video_yres = '.yres 480'
        elif vr == '800x600':
            video_xres = '.xres 800'
            video_yres = '.yres 600'
        elif vr == '960x720':
            video_xres = '.xres 960'
            video_yres = '.yres 720'
        elif vr == '1024x768':
            video_xres = '.xres 1024'
            video_yres = '.yres 768'
        elif vr == '1366x768':
            video_xres = '.xres 1366'
            video_yres = '.yres 768'
            
    def spuresample(self):
        global spu_resample
        global scsp_resample
        global rs
        rs = self.sldSPUresample.value()
        if rs == 0:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 0'
            scsp_resample = '.scsp.resamp_quality 0'
        elif rs == 1:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 1'
            scsp_resample = '.scsp.resamp_quality 1'
        elif rs == 2:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 2'
            scsp_resample = '.scsp.resamp_quality 2'
        elif rs == 3:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 3'
            scsp_resample = '.scsp.resamp_quality 3'
        elif rs == 4:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 4'
            scsp_resample = '.scsp.resamp_quality 4'
        elif rs == 5:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 5'
            scsp_resample = '.scsp.resamp_quality 5'
        elif rs == 6:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 6'
            scsp_resample = '.scsp.resamp_quality 6'
        elif rs == 7:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 7'
            scsp_resample = '.scsp.resamp_quality 7'
        elif rs == 8:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 8'
            scsp_resample = '.scsp.resamp_quality 8'
        elif rs == 9:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 9'
            scsp_resample = '.scsp.resamp_quality 9'
        elif rs == 10:
            self.lbSPUvalue.setNum(rs)
            spu_resample = '.spu.resamp_quality 10'
            scsp_resample = '.scsp.resamp_quality 10'
            
    def videodriver(self):
        global video_driver
        global vd 
        vd =self.cmbVideoDriver.currentText()
        if vd == 'SDL':
            video_driver = '--video.driver sdl'
        elif vd == 'OpenGL':
            video_driver = '--video.driver opengl'
    
    def videopix(self):
        global video_pix
        global vp
        vp = self.cmbVideoPix.currentText()
        if vp == 'None':
            video_pix = '.pixshader none'
        elif vp == 'Autoip':
            video_pix = '.pixshader autoip'
        elif vp == 'Autoip Sharper':
            video_pix = '.pixshader autoipsharper'
        elif vp == 'IpSharper':
            video_pix = '.pixshader ipsharper'
        elif vp == 'SABR':
            video_pix = '.pixshader sabr'
            
    def videostretch(self):
        global video_stretch
        global vs
        vs = self.cmbAspect.currentText()
        if vs == 'Aspect Full':
            video_stretch = '.stretch full'
        elif vs == 'Aspect':
            video_stretch = '.stretch aspect'
        elif vs == 'Aspect Int':
            video_stretch = '.stretch aspect_int'
        elif vs == 'Aspect Mult2':
            video_stretch = '.stretch aspect_mult2'
        elif vs == 'Aspect 0':
            video_stretch = '.stretch 0'
            
    def videospecial(self):
        global video_special
        global vsp
        vsp =self.cmbVideoSpecial.currentText()    
        if vsp == 'None':
            video_special = '.special none'
        elif vsp == '2xsai':
            video_special = '.special 2xsai'
        elif vsp == 'Super2xsai':
            video_special = '.special super2xsai'
        elif vsp == 'Supereagle':
            video_special = '.special supereagle'
        elif vsp == 'Hq2x':
            video_special = '.special hq2x'
            
    def videoxscale(self):
        global video_xscale
        global vx
        vx = self.cmbXscale.currentText()
        if vx == '0.20':
            video_xscale = '.xscale 0.20'
        elif vx == '0.40':
            video_xscale = '.xscale 0.40'
        elif vx == '0.60':
            video_xscale = '.xscale 0.60'
        elif vx == '0.80':
            video_xscale = '.xscale 0.80'
        elif vx == '1':
            video_xscale = '.xscale 1'
        elif vx == '2':
            video_xscale = '.xscale 2'
        elif vx == '3':
            video_xscale = '.xscale 3'
            
    def videoyscale(self):
        global video_yscale
        global vy
        vy = self.cmbYscale.currentText()
        if vy == '0.20':
            video_yscale = '.yscale 0.20'
        elif vy == '0.40':
            video_yscale = '.yscale 0.40'
        elif vy == '0.60':
            video_yscale = '.yscale 0.60'
        elif vy == '0.80':
            video_yscale = '.yscale 0.80'
        elif vy == '1':
            video_yscale = '.yscale 1'
        elif vy == '2':
            video_yscale = '.yscale 2'
        elif vy == '3':
            video_yscale = '.yscale 3'
            
    def videoxscaleFS(self):
        global video_xscalefs
        global vxf
        vxf = self.cmbXscaleFS.currentText()
        if vxf == '0.20':
            video_xscalefs = '.xscalefs 0.20'
        elif vxf == '0.40':
            video_xscalefs = '.xscalefs 0.40'
        elif vxf == '0.60':
            video_xscalefs = '.xscalefs 0.60'
        elif vxf == '0.80':
            video_xscalefs = '.xscalefs 0.80'
        elif vxf == '1':
            video_xscalefs = '.xscalefs 1'
        elif vxf == '2':
            video_xscalefs = '.xscale 2'
        elif vxf == '3':
            video_xscalefs = '.xscalefs 3'
            
    def videoyscaleFS(self):
        global video_yscalefs
        global vyf
        vyf = self.cmbYscaleFS.currentText()
        if vyf == '0.20':
            video_yscalefs = '.yscalefs 0.20'
        elif vyf == '0.40':
            video_yscalefs = '.yscalefs 0.40'
        elif vyf == '0.60':
            video_yscalefs = '.yscalefs 0.60'
        elif vyf == '0.80':
            video_yscalefs = '.yscalefs 0.80'
        elif vyf == '1':
            video_yscalefs = '.yscalefs 1'
        elif vyf == '2':
            video_yscalefs = '.yscalefs 2'
        elif vyf == '3':
            video_yscalefs = '.yscalefs 3'
            
    def recordConfig(self):
        global emu
        emu = self.edMednafen.text()   
        global comando_snes
        global comando_gens
        global comando_nes
        global comando_sms
        global comando_psx
        global comando_sat
        comando_snes = "%s %s %s %s %s --snes%s "\
                                            "--snes%s %s "\
                                            "--snes%s "\
                                            "--snes%s "\
                                            "--snes%s --snes%s "\
                                            "--snes%s --snes%s " \
                                            "--snes%s --snes%s" %(emu,sound_driver,
                                                         sound_device,
                                                         sound_rate,
                                                         video_driver,
                                                         video_pix,
                                                         video_bilinear,
                                                         videofs,
                                                         video_stretch,
                                                         video_special,
                                                         video_xres,
                                                         video_yres,
                                                         video_xscale,
                                                         video_yscale,
                                                         video_xscalefs,
                                                         video_yscalefs)
        comando_gens = "%s %s %s %s %s --md%s "\
                                            "--md%s %s "\
                                            "--md%s --md%s "\
                                            "--md%s --md%s " \
                                            "--md%s --md%s " \
                                            "--md%s --md%s" %(emu,sound_driver,
                                                              sound_device,
                                                              sound_rate,
                                                              video_driver,
                                                              video_pix,
                                                              video_bilinear,
                                                              videofs,
                                                              video_stretch,
                                                              video_special,
                                                              video_xres,
                                                              video_yres,
                                                              video_xscale,
                                                              video_yscale,
                                                              video_xscalefs,
                                                              video_yscalefs)
        comando_nes = "%s %s %s %s %s --nes%s "\
                                           "--nes%s %s "\
                                           "--nes%s --nes%s "\
                                           "--nes%s --nes%s " \
                                           "--nes%s --nes%s " \
                                           "--nes%s --nes%s" %(emu,sound_driver,
                                                               sound_device,
                                                               sound_rate,
                                                               video_driver,
                                                               video_pix,
                                                               video_bilinear,
                                                               videofs,
                                                               video_stretch,
                                                               video_special,
                                                               video_xres,
                                                               video_yres,
                                                               video_xscale,
                                                               video_yscale,
                                                               video_xscalefs,
                                                               video_yscalefs)
        comando_sms = "%s %s %s %s %s --sms%s "\
                                           "--sms%s %s "\
                                           "--sms%s --sms%s "\
                                           "--sms%s --sms%s "\
                                           "--sms%s --sms%s "\
                                           "--sms%s --sms%s" %(emu,sound_driver,
                                                               sound_device,
                                                               sound_rate,
                                                               video_driver,
                                                               video_pix,
                                                               video_bilinear,
                                                               videofs,
                                                               video_stretch,
                                                               video_special,
                                                               video_xres,
                                                               video_yres,
                                                               video_xscale,
                                                               video_yscale,
                                                               video_xscalefs,
                                                               video_yscalefs)
        comando_psx = "%s %s %s %s %s %s %s --psx%s "\
                                           "--psx%s --psx%s %s "\
                                           "--psx%s --psx%s "\
                                           "--psx%s --psx%s "\
                                           "--psx%s --psx%s "\
                                           "--psx%s --psx%s" %(emu,sound_driver,
                                                               video_sync,
                                                               time_sync,
                                                               sound_device,
                                                               sound_rate,
                                                               video_driver,
                                                               spu_resample,
                                                               video_pix,
                                                               video_bilinear,
                                                               videofs,
                                                               video_stretch,
                                                               video_special,
                                                               video_xres,
                                                               video_yres,
                                                               video_xscale,
                                                               video_yscale,
                                                               video_xscalefs,
                                                               video_yscalefs)
        comando_sat = "%s %s %s %s %s %s %s --ss%s "\
                                           "--ss%s --ss%s %s "\
                                           "--ss%s --ss%s "\
                                           "--ss%s --ss%s "\
                                           "--ss%s --ss%s "\
                                           "--ss%s --ss%s" %(emu,sound_driver,
                                                               video_sync,
                                                               time_sync,
                                                               sound_device,
                                                               sound_rate,
                                                               video_driver,
                                                               scsp_resample,
                                                               video_pix,
                                                               video_bilinear,
                                                               videofs,
                                                               video_stretch,
                                                               video_special,
                                                               video_xres,
                                                               video_yres,
                                                               video_xscale,
                                                               video_yscale,
                                                               video_xscalefs,
                                                               video_yscalefs)
        
        config.set("EMUL", "EMU", emu)
        config.set("COMMAND_PATH", "SNES_RUN", comando_snes)
        config.set("COMMAND_PATH", "GEN_RUN", comando_gens)
        config.set("COMMAND_PATH", "NES_RUN", comando_nes)
        config.set("COMMAND_PATH", "SMS_RUN", comando_sms)
        config.set("COMMAND_PATH", "PSX_RUN", comando_psx)
        config.set("COMMAND_PATH", "SAT_RUN", comando_sat)
        arquivo_cfg = open(".qtnafen.cfg", "w")
        config.write(arquivo_cfg)
        arquivo_cfg.close()
        
        config.read(".qtnafen.cfg")

        emu = config.get("EMUL", "EMU")

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

###############################################################################

    def aplicar(self):
        if self.edMednafen.text() == '':
            QtGui.QMessageBox.information(None, "Informação", "Selecione o emulador")
            self.edMednafen.setFocus()
            return
        
        self.bilinear()
        self.videosync()
        self.timesync()
        self.video_fs()
        self.sounddriver()
        self.sounddevice()
        self.soundrate()
        self.videores()
        self.spuresample()
        self.videodriver()
        self.videopix()
        self.videostretch()
        self.videospecial()
        self.videoxscale()
        self.videoyscale()
        self.videoxscaleFS()
        self.videoyscaleFS()
        self.recordConfig()
        self.fechar()
        
        
    
        
###############################################################################

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ConfigDialog = QtGui.QDialog()
    ui = Ui_ConfigDialog()
    ui.setupUi(ConfigDialog)
    ConfigDialog.show()
    sys.exit(app.exec_())

