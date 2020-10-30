# -*- coding: utf-8 -*-

from PyQt5 import uic, QtWidgets


def chama_segunda_tela():
    primeira_tela.hide()
    segunda_tela.show()
    terceira_tela.show()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("untitled.ui")
segunda_tela = uic.loadUi("form_prop.ui")
terceira_tela = uic.loadUi("form_ender.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela)

primeira_tela.show()
app.exec()
