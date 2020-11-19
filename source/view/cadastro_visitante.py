# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_visitante, menu
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import center_screen
from PyQt5.QtWidgets import QLineEdit

# Example of a funcion assigned to a button:

print(type(cadastro_visitante.line_nome_visitante))


def teste():
    cadastro_visitante.hide()
    menu.show()


cadastro_visitante.salvar_visitante.clicked.connect(teste)
cadastro_visitante.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastro_visitante)
na = cadastro_visitante.findChild(QLineEdit)
