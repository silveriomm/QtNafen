# -*- coding: utf-8 -*-

msg_about = u"""Um simples frontend para o Mednafen\n
Silvério Mantovaneli\n
silveriomm@bol.com.br\n
Vila Valério - ES - Brasil\n
2016"""

from PySide import QtCore, QtGui
from os import popen
import os, fnmatch
import ConfigParser
config = ConfigParser.ConfigParser()

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 400)
        MainWindow.setMinimumSize(QtCore.QSize(750, 400))
        MainWindow.setMaximumSize(QtCore.QSize(750, 400))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWindow = QtGui.QTabWidget(self.centralwidget)
        self.tabWindow.setGeometry(QtCore.QRect(0, 0, 751, 361))
        self.tabWindow.setIconSize(QtCore.QSize(96, 24))
        self.tabWindow.setObjectName("tabWindow")
        self.tabSnes = QtGui.QWidget()
        self.tabSnes.setObjectName("tabSnes")
        self.widget = QtGui.QWidget(self.tabSnes)
        self.widget.setGeometry(QtCore.QRect(0, 0, 740, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btPlaySnes = QtGui.QPushButton(self.widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btPlaySnes.setIcon(icon)
        self.btPlaySnes.setObjectName("btPlaySnes")
        self.horizontalLayout.addWidget(self.btPlaySnes)
        self.edFiltraSnes = QtGui.QLineEdit(self.widget)
        self.edFiltraSnes.setObjectName("edFiltraSnes")
        self.horizontalLayout.addWidget(self.edFiltraSnes)
        self.btClearSnes = QtGui.QPushButton(self.widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btClearSnes.setIcon(icon1)
        self.btClearSnes.setObjectName("btClearSnes")
        self.horizontalLayout.addWidget(self.btClearSnes)
        self.lstSnes = QtGui.QListWidget(self.tabSnes)
        self.lstSnes.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.lstSnes.setObjectName("lstSnes")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/icons/snes_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWindow.addTab(self.tabSnes, icon2, "")
        self.tabGenesis = QtGui.QWidget()
        self.tabGenesis.setObjectName("tabGenesis")
        self.widget_2 = QtGui.QWidget(self.tabGenesis)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 740, 41))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btPlayGenesis = QtGui.QPushButton(self.widget_2)
        self.btPlayGenesis.setIcon(icon)
        self.btPlayGenesis.setObjectName("btPlayGenesis")
        self.horizontalLayout_2.addWidget(self.btPlayGenesis)
        self.edFiltraGenesis = QtGui.QLineEdit(self.widget_2)
        self.edFiltraGenesis.setObjectName("edFiltraGenesis")
        self.horizontalLayout_2.addWidget(self.edFiltraGenesis)
        self.btClearGenesis = QtGui.QPushButton(self.widget_2)
        self.btClearGenesis.setIcon(icon1)
        self.btClearGenesis.setObjectName("btClearGenesis")
        self.horizontalLayout_2.addWidget(self.btClearGenesis)
        self.lstGenesis = QtGui.QListWidget(self.tabGenesis)
        self.lstGenesis.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.lstGenesis.setObjectName("lstGenesis")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/icons/genesis_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWindow.addTab(self.tabGenesis, icon3, "")
        self.tabNes = QtGui.QWidget()
        self.tabNes.setObjectName("tabNes")
        self.widget_3 = QtGui.QWidget(self.tabNes)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 740, 41))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btPlayNes = QtGui.QPushButton(self.widget_3)
        self.btPlayNes.setIcon(icon)
        self.btPlayNes.setObjectName("btPlayNes")
        self.horizontalLayout_3.addWidget(self.btPlayNes)
        self.edFiltraNes = QtGui.QLineEdit(self.widget_3)
        self.edFiltraNes.setObjectName("edFiltraNes")
        self.horizontalLayout_3.addWidget(self.edFiltraNes)
        self.btClearNes = QtGui.QPushButton(self.widget_3)
        self.btClearNes.setIcon(icon1)
        self.btClearNes.setObjectName("btClearNes")
        self.horizontalLayout_3.addWidget(self.btClearNes)
        self.lstNes = QtGui.QListWidget(self.tabNes)
        self.lstNes.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.lstNes.setObjectName("lstNes")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/icons/famicom_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWindow.addTab(self.tabNes, icon4, "")
        self.tabSms = QtGui.QWidget()
        self.tabSms.setObjectName("tabSms")
        self.widget_4 = QtGui.QWidget(self.tabSms)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 740, 41))
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btPlaySms = QtGui.QPushButton(self.widget_4)
        self.btPlaySms.setIcon(icon)
        self.btPlaySms.setObjectName("btPlaySms")
        self.horizontalLayout_4.addWidget(self.btPlaySms)
        self.edFiltraSms = QtGui.QLineEdit(self.widget_4)
        self.edFiltraSms.setObjectName("edFiltraSms")
        self.horizontalLayout_4.addWidget(self.edFiltraSms)
        self.btClearSms = QtGui.QPushButton(self.widget_4)
        self.btClearSms.setIcon(icon1)
        self.btClearSms.setObjectName("btClearSms")
        self.horizontalLayout_4.addWidget(self.btClearSms)
        self.lstSms = QtGui.QListWidget(self.tabSms)
        self.lstSms.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.lstSms.setObjectName("lstSms")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/icons/master-system-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWindow.addTab(self.tabSms, icon5, "")
        self.tabPsx = QtGui.QWidget()
        self.tabPsx.setObjectName("tabPsx")
        self.widget_5 = QtGui.QWidget(self.tabPsx)
        self.widget_5.setGeometry(QtCore.QRect(0, 0, 740, 41))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btPlayPsx = QtGui.QPushButton(self.widget_5)
        self.btPlayPsx.setIcon(icon)
        self.btPlayPsx.setObjectName("btPlayPsx")
        self.horizontalLayout_5.addWidget(self.btPlayPsx)
        self.edFiltraPsx = QtGui.QLineEdit(self.widget_5)
        self.edFiltraPsx.setObjectName("edFiltraPsx")
        self.horizontalLayout_5.addWidget(self.edFiltraPsx)
        self.btClearPsx = QtGui.QPushButton(self.widget_5)
        self.btClearPsx.setIcon(icon1)
        self.btClearPsx.setObjectName("btClearPsx")
        self.horizontalLayout_5.addWidget(self.btClearPsx)
        self.lstPsx = QtGui.QListWidget(self.tabPsx)
        self.lstPsx.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.lstPsx.setObjectName("lstPsx")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/icons/psx_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWindow.addTab(self.tabPsx, icon6, "")
        self.tabSaturn = QtGui.QWidget()
        self.tabSaturn.setObjectName("tabSaturn")
        self.widget_6 = QtGui.QWidget(self.tabSaturn)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 740, 41))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btPlaySaturn = QtGui.QPushButton(self.widget_6)
        self.btPlaySaturn.setIcon(icon)
        self.btPlaySaturn.setObjectName("btPlaySaturn")
        self.horizontalLayout_6.addWidget(self.btPlaySaturn)
        self.edFiltraSaturn = QtGui.QLineEdit(self.widget_6)
        self.edFiltraSaturn.setObjectName("edFiltraSaturn")
        self.horizontalLayout_6.addWidget(self.edFiltraSaturn)
        self.btClearSaturn = QtGui.QPushButton(self.widget_6)
        self.btClearSaturn.setIcon(icon1)
        self.btClearSaturn.setObjectName("btClearSaturn")
        self.horizontalLayout_6.addWidget(self.btClearSaturn)
        self.lstSaturn = QtGui.QListWidget(self.tabSaturn)
        self.lstSaturn.setGeometry(QtCore.QRect(10, 40, 721, 281))
        self.lstSaturn.setObjectName("lstSaturn")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/icons/saturn_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWindow.addTab(self.tabSaturn, icon7, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuConfigura_es = QtGui.QMenu(self.menubar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        self.menuAjuda = QtGui.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_rom = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir_rom.setIcon(icon8)
        self.actionAbrir_rom.setObjectName("actionAbrir_rom")
        self.actionSelecionaDiretorios = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/icons/directory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelecionaDiretorios.setIcon(icon9)
        self.actionSelecionaDiretorios.setObjectName("actionSelecionaDiretorios")
        self.actionAtualiza_lista_de_jogos = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAtualiza_lista_de_jogos.setIcon(icon10)
        self.actionAtualiza_lista_de_jogos.setObjectName("actionAtualiza_lista_de_jogos")
        self.actionSair = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/img/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSair.setIcon(icon11)
        self.actionSair.setObjectName("actionSair")
        self.actionConfiguracoes = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/img/icons/config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfiguracoes.setIcon(icon12)
        self.actionConfiguracoes.setObjectName("actionConfiguracoes")
        self.actionLimpar_lista_de_jogos = QtGui.QAction(MainWindow)
        self.actionLimpar_lista_de_jogos.setIcon(icon1)
        self.actionLimpar_lista_de_jogos.setObjectName("actionLimpar_lista_de_jogos")
        self.actionSobre_o_QtNafen = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/img/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSobre_o_QtNafen.setIcon(icon13)
        self.actionSobre_o_QtNafen.setObjectName("actionSobre_o_QtNafen")
        self.menuArquivo.addAction(self.actionAbrir_rom)
        self.menuArquivo.addAction(self.actionSelecionaDiretorios)
        self.menuArquivo.addAction(self.actionAtualiza_lista_de_jogos)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menuConfigura_es.addAction(self.actionConfiguracoes)
        self.menuConfigura_es.addSeparator()
        self.menuConfigura_es.addAction(self.actionLimpar_lista_de_jogos)
        self.menuAjuda.addAction(self.actionSobre_o_QtNafen)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuConfigura_es.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWindow.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionSair, QtCore.SIGNAL("activated()"), MainWindow.close)
        QtCore.QObject.connect(self.actionAbrir_rom, QtCore.SIGNAL("activated()"), self.openRom)
        QtCore.QObject.connect(self.actionAtualiza_lista_de_jogos, QtCore.SIGNAL("activated()"), self.refreshList)
        QtCore.QObject.connect(self.actionConfiguracoes, QtCore.SIGNAL("activated()"), self.openConfigDialog)
        QtCore.QObject.connect(self.actionLimpar_lista_de_jogos, QtCore.SIGNAL("activated()"), self.clearList)
        QtCore.QObject.connect(self.actionSelecionaDiretorios, QtCore.SIGNAL("activated()"), self.openDirectory)
        QtCore.QObject.connect(self.actionSobre_o_QtNafen, QtCore.SIGNAL("activated()"), self.about)
        QtCore.QObject.connect(self.btClearGenesis, QtCore.SIGNAL("clicked()"), self.clearGenesis)
        QtCore.QObject.connect(self.btClearNes, QtCore.SIGNAL("clicked()"), self.clearNes)
        QtCore.QObject.connect(self.btClearPsx, QtCore.SIGNAL("clicked()"), self.clearPsx)
        QtCore.QObject.connect(self.btClearSaturn, QtCore.SIGNAL("clicked()"), self.clearSaturn)
        QtCore.QObject.connect(self.btClearSms, QtCore.SIGNAL("clicked()"), self.clearSms)
        QtCore.QObject.connect(self.btClearSnes, QtCore.SIGNAL("clicked()"), self.clearSnes)
        QtCore.QObject.connect(self.btPlayGenesis, QtCore.SIGNAL("clicked()"), self.playGenesis)
        QtCore.QObject.connect(self.btPlayNes, QtCore.SIGNAL("clicked()"), self.playNes)
        QtCore.QObject.connect(self.btPlayPsx, QtCore.SIGNAL("clicked()"), self.playPsx)
        QtCore.QObject.connect(self.btPlaySaturn, QtCore.SIGNAL("clicked()"), self.playSaturn)
        QtCore.QObject.connect(self.btPlaySms, QtCore.SIGNAL("clicked()"), self.playSms)
        QtCore.QObject.connect(self.btPlaySnes, QtCore.SIGNAL("clicked()"), self.playSnes)
        QtCore.QObject.connect(self.edFiltraSnes, QtCore.SIGNAL("textChanged(QString)"), self.updateListSnes)
        QtCore.QObject.connect(self.edFiltraGenesis, QtCore.SIGNAL("textChanged(QString)"), self.updateListGenesis)
        QtCore.QObject.connect(self.edFiltraNes, QtCore.SIGNAL("textChanged(QString)"), self.updateListNes)
        QtCore.QObject.connect(self.edFiltraPsx, QtCore.SIGNAL("textChanged(QString)"), self.updateListPsx)
        QtCore.QObject.connect(self.edFiltraSaturn, QtCore.SIGNAL("textChanged(QString)"), self.updateListSaturn)
        QtCore.QObject.connect(self.edFiltraSms, QtCore.SIGNAL("textChanged(QString)"), self.updateListSms)
        QtCore.QObject.connect(self.lstGenesis, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.playGenesis)
        QtCore.QObject.connect(self.lstNes, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.playNes)
        QtCore.QObject.connect(self.lstPsx, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.playPsx)
        QtCore.QObject.connect(self.lstSaturn, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.playSaturn)
        QtCore.QObject.connect(self.lstSms, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.playSms)
        QtCore.QObject.connect(self.lstSnes, QtCore.SIGNAL("doubleClicked(QModelIndex)"), self.playSnes)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "QtNafen - Mednafen Frontend", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSnes.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/snes_logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlaySnes.setText(QtGui.QApplication.translate("MainWindow", "Jogar", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearSnes.setText(QtGui.QApplication.translate("MainWindow", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWindow.setTabToolTip(self.tabWindow.indexOf(self.tabSnes), QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/snes_logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlayGenesis.setText(QtGui.QApplication.translate("MainWindow", "Jogar", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearGenesis.setText(QtGui.QApplication.translate("MainWindow", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWindow.setTabToolTip(self.tabWindow.indexOf(self.tabGenesis), QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/genesis_logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlayNes.setText(QtGui.QApplication.translate("MainWindow", "Jogar", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearNes.setText(QtGui.QApplication.translate("MainWindow", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWindow.setTabToolTip(self.tabWindow.indexOf(self.tabNes), QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/famicom_logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlaySms.setText(QtGui.QApplication.translate("MainWindow", "Jogar", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearSms.setText(QtGui.QApplication.translate("MainWindow", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWindow.setTabToolTip(self.tabWindow.indexOf(self.tabSms), QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/master-system-logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlayPsx.setText(QtGui.QApplication.translate("MainWindow", "Jogar", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearPsx.setText(QtGui.QApplication.translate("MainWindow", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWindow.setTabToolTip(self.tabWindow.indexOf(self.tabPsx), QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/psx_logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlaySaturn.setText(QtGui.QApplication.translate("MainWindow", "Jogar", None, QtGui.QApplication.UnicodeUTF8))
        self.btClearSaturn.setText(QtGui.QApplication.translate("MainWindow", "Limpar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWindow.setTabToolTip(self.tabWindow.indexOf(self.tabSaturn), QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/img/icons/saturn_logo.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArquivo.setTitle(QtGui.QApplication.translate("MainWindow", "Arquivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfigura_es.setTitle(QtGui.QApplication.translate("MainWindow", "Opções", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAjuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ajuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir_rom.setText(QtGui.QApplication.translate("MainWindow", "Abrir rom...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelecionaDiretorios.setText(QtGui.QApplication.translate("MainWindow", "Selecionar diretórios", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAtualiza_lista_de_jogos.setText(QtGui.QApplication.translate("MainWindow", "Atualizar lista de jogos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSair.setText(QtGui.QApplication.translate("MainWindow", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfiguracoes.setText(QtGui.QApplication.translate("MainWindow", "Configurações", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLimpar_lista_de_jogos.setText(QtGui.QApplication.translate("MainWindow", "Limpar lista de jogos", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSobre_o_QtNafen.setText(QtGui.QApplication.translate("MainWindow", "Sobre o QtNafen", None, QtGui.QApplication.UnicodeUTF8))

        self.listaSnes()
        self.listaGenesis()
        self.listaNes()
        self.listaSms()
        self.listaPsx()
        self.listaSaturn()

# ===============================================================================================================================================
 
    def updateCommand(self):
        global dir_snes
        global dir_gen
        global dir_nes
        global dir_sms
        global dir_psx
        global dir_sat
        global comando_snes
        global comando_gens
        global comando_nes
        global comando_sms
        global comando_psx
        global comando_sat
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
     
    def clearSnes(self):
        self.edFiltraSnes.clear()

    def clearGenesis(self):
        self.edFiltraGenesis.clear()

    def clearNes(self):
        self.edFiltraNes.clear()

    def clearSms(self):
        self.edFiltraSms.clear()

    def clearPsx(self):
        self.edFiltraPsx.clear()

    def clearSaturn(self):
        self.edFiltraSaturn.clear()

    def updateListSnes(self):
        i = 0
        snes_roms=[]
        for filename in sorted(fnmatch.filter(os.listdir(dir_snes),'*.sfc')):
            snes_roms.append(filename)
            i = i + 1
        for filename in sorted(fnmatch.filter(os.listdir(dir_snes),'*.zip')):
            snes_roms.append(filename)
            i = i + 1
        search_term = self.edFiltraSnes.text()
        if search_term == "":
            self.lstSnes.clear()
            self.listaSnes()
        else:
            self.lstSnes.clear()
            for item in snes_roms:
                if search_term.lower() in item.lower():
                    self.lstSnes.addItem(item)

    def updateListGenesis(self):
        i = 0
        gen_roms=[]
        for filename in sorted(fnmatch.filter(os.listdir(dir_gen),'*.md')):
            gen_roms.append(filename)
            i = i + 1
        for filename in sorted(fnmatch.filter(os.listdir(dir_gen),'*.zip')):
            gen_roms.append(filename)
            i = i + 1
        search_term = self.edFiltraGenesis.text()
        if search_term == "":
            self.lstGenesis.clear()
            self.listaGenesis()
        else:
            self.lstGenesis.clear()
            for item in gen_roms:
                if search_term.lower() in item.lower():
                    self.lstGenesis.addItem(item)

    def updateListNes(self):
        i = 0
        nes_roms=[]
        for filename in sorted(fnmatch.filter(os.listdir(dir_nes),'*.nes')):
            nes_roms.append(filename)
            i = i + 1
        for filename in sorted(fnmatch.filter(os.listdir(dir_nes),'*.zip')):
            nes_roms.append(filename)
            i = i + 1
        search_term = self.edFiltraNes.text()
        if search_term == "":
            self.lstNes.clear()
            self.listaNes()
        else:
            self.lstNes.clear()
            for item in nes_roms:
                if search_term.lower() in item.lower():
                    self.lstNes.addItem(item)

    def updateListSms(self):
        i = 0
        sms_roms=[]
        for filename in sorted(fnmatch.filter(os.listdir(dir_sms),'*.sms')):
            sms_roms.append(filename)
            i = i + 1
        for filename in sorted(fnmatch.filter(os.listdir(dir_sms),'*.zip')):
            sms_roms.append(filename)
            i = i + 1
        search_term = self.edFiltraSms.text()
        if search_term == "":
            self.lstSms.clear()
            self.listaSms()
        else:
            self.lstSms.clear()
            for item in sms_roms:
                if search_term.lower() in item.lower():
                    self.lstSms.addItem(item)

    def updateListPsx(self):
        i = 0
        psx_roms=[]
        for filename in sorted(fnmatch.filter(os.listdir(dir_psx),'*.cue')):
            psx_roms.append(filename)
            i = i + 1
        for filename in sorted(fnmatch.filter(os.listdir(dir_psx),'*.ccd')):
            psx_roms.append(filename)
            i = i + 1
        search_term = self.edFiltraPsx.text()
        if search_term == "":
            self.lstPsx.clear()
            self.listaPsx()
        else:
            self.lstPsx.clear()
            for item in psx_roms:
                if search_term.lower() in item.lower():
                    self.lstPsx.addItem(item)

    def updateListSaturn(self):
        i = 0
        sat_roms=[]
        for filename in sorted(fnmatch.filter(os.listdir(dir_sat),'*.cue')):
            sat_roms.append(filename)
            i = i + 1
        for filename in sorted(fnmatch.filter(os.listdir(dir_sat),'*.ccd')):
            sat_roms.append(filename)
            i = i + 1
        search_term = self.edFiltraSaturn.text()
        if search_term == "":
            self.lstSaturn.clear()
            self.listaSaturn()
        else:
            self.lstSaturn.clear()
            for item in sat_roms:
                if search_term.lower() in item.lower():
                    self.lstSaturn.addItem(item)

    def playSnes(self):
        row = self.lstSnes.currentRow()
        rom = self.lstSnes.item(row).text()
        file = comando_snes + ' "' + dir_snes + '\\' + rom + '"'
        popen(file)

    def playGenesis(self):
        row = self.lstGenesis.currentRow()
        rom = self.lstGenesis.item(row).text()
        file = comando_gens + ' "' + dir_gen + '\\' + rom + '"'
        popen(file)
        
    def playNes(self):
        row = self.lstNes.currentRow()
        rom = self.lstNes.item(row).text()
        file = comando_nes + ' "' + dir_nes + '\\' + rom + '"'
        popen(file)
        
    def playSms(self):
        row = self.lstSms.currentRow()
        rom = self.lstSms.item(row).text()
        file = comando_sms + ' "' + dir_sms + '\\' + rom + '"'
        popen(file)
        
    def playPsx(self):
        row = self.lstPsx.currentRow()
        rom = self.lstPsx.item(row).text()
        file = comando_psx + ' "' + dir_psx + '\\' + rom + '"'
        popen(file)
        
    def playSaturn(self):
        row = self.lstSaturn.currentRow()
        rom = self.lstSaturn.item(row).text()
        file = comando_sat + ' "' + dir_sat + '\\' + rom + '"'
        popen(file)

    def openDirectory(self):
        try:
            popen('DirDialog.pyw')
        finally:
            MainWindow.show()

    def openConfigDialog(self):
        try:
            popen('ConfigDialog.pyw')
        finally:
            self.updateCommand()
            MainWindow.show()

    def refreshList(self):
        self.updateCommand()
        self.lstSnes.clear()
        self.lstGenesis.clear()
        self.lstNes.clear()
        self.lstSms.clear()
        self.lstPsx.clear()
        self.lstSaturn.clear()
        self.listaSnes()
        self.listaGenesis()
        self.listaNes()
        self.listaSms()
        self.listaPsx()
        self.listaSaturn()

    def openRom(self):
        filename = QtGui.QFileDialog.getOpenFileName(None, "Abrir arquivo rom", "~/",
                                                    "Todos os arquivos (*)")
        popen(emu+' "'+str(filename[0])+'"')

    def about(self):
        QtGui.QMessageBox.information(None, "Sobre o QtNafen", msg_about)

    def listaSnes(self):
        if dir_snes == "":
            pass
        else:
            i = 0
            for filename in sorted(fnmatch.filter(os.listdir(dir_snes),
                                                                  '*.sfc')):
                self.lstSnes.addItem(filename)
                i = i + 1
            for filename in sorted(fnmatch.filter(os.listdir(dir_snes),
                                                                  '*.zip')):
                self.lstSnes.addItem(filename)
                i = i + 1
        arquivo_cfg.close()

    def listaGenesis(self):
        if dir_gen == "":
            pass
        else:
            i = 0
            for filename in sorted(fnmatch.filter(os.listdir(dir_gen),
                                                                  '*.md')):
                self.lstGenesis.addItem(filename)
                i = i + 1
            for filename in sorted(fnmatch.filter(os.listdir(dir_gen),
                                                                  '*.zip')):
                self.lstGenesis.addItem(filename)
                i = i + 1
        arquivo_cfg.close()

    def listaNes(self):
        if dir_nes == "":
            pass
        else:
            i = 0
            for filename in sorted(fnmatch.filter(os.listdir(dir_nes),
                                                                  '*.nes')):
                self.lstNes.addItem(filename)
                i = i + 1
            for filename in sorted(fnmatch.filter(os.listdir(dir_nes),
                                                                  '*.zip')):
                self.lstNes.addItem(filename)
                i = i + 1
        arquivo_cfg.close()

    def listaSms(self):
        if dir_sms == "":
            pass
        else:
            i = 0
            for filename in sorted(fnmatch.filter(os.listdir(dir_sms),
                                                                  '*.sms')):
                self.lstSms.addItem(filename)
                i = i + 1
            for filename in sorted(fnmatch.filter(os.listdir(dir_sms),
                                                                  '*.zip')):
                self.lstSms.addItem(filename)
                i = i + 1
        arquivo_cfg.close()

    def listaPsx(self):
        if dir_psx == "":
            pass
        else:
            i = 0
            for filename in sorted(fnmatch.filter(os.listdir(dir_psx),
                                                                  '*.cue')):
                self.lstPsx.addItem(filename)
                i = i + 1
            for filename in sorted(fnmatch.filter(os.listdir(dir_psx),
                                                                  '*.ccd')):
                self.lstPsx.addItem(filename)
                i = i + 1
        arquivo_cfg.close()

    def listaSaturn(self):
        if dir_sat == "":
            pass
        else:
            i = 0
            for filename in sorted(fnmatch.filter(os.listdir(dir_sat),
                                                                  '*.cue')):
                self.lstSaturn.addItem(filename)
                i = i + 1
            for filename in sorted(fnmatch.filter(os.listdir(dir_sat),
                                                                  '*.ccd')):
                self.lstSaturn.addItem(filename)
                i = i + 1
        arquivo_cfg.close()

    def clearList(self):
        self.lstSnes.clear()
        self.lstGenesis.clear()
        self.lstNes.clear()
        self.lstSms.clear()
        self.lstPsx.clear()
        self.lstSaturn.clear()
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

import img_icons_qrc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

