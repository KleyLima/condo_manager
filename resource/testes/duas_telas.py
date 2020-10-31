# -*- coding: utf-8 -*-

from PyQt5 import uic, QtWidgets
from os import environ
from resource.testes.telas import *

def chama_segunda_tela():
    primeira_tela.hide()
    locador.show()
    terceira_tela.show()
    menu.show()


primeira_tela.pushButton.clicked.connect(chama_segunda_tela)

primeira_tela.show()
app.exec()
