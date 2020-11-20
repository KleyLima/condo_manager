# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, controle_material, menu
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen

# Example of a funcion assigned to a button:


def teste():
    print("MENU")
    controle_material.hide()
    menu.show()


controle_material.b_menu.clicked.connect(teste)
controle_material.setWindowFlag(Qt.FramelessWindowHint)
center_screen(controle_material)
