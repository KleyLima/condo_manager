# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_visitante, menu
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen

# Example of a funcion assigned to a button:


def teste():
    cadastro_visitante.hide()
    menu.show()


cadastro_visitante.salvar_visitante.clicked.connect(teste)
cadastro_visitante.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(cadastro_visitante)
