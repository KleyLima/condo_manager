# -*- coding: utf-8 -*-

from PyQt5 import uic, QtWidgets
from os import environ

def chama_segunda_tela():
    primeira_tela.hide()
    segunda_tela.show()
    terceira_tela.show()


app = QtWidgets.QApplication([])
source_interface = environ.get("PYTHONPATH") + "/resource/testes/"
primeira_tela = uic.loadUi(source_interface + "untitled.ui")
segunda_tela = uic.loadUi(source_interface + "form_prop.ui")
terceira_tela = uic.loadUi(source_interface + "form_ender.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela)

primeira_tela.show()
app.exec()
