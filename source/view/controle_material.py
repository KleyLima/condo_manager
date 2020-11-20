# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, controle_material, menu
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, clear_and_exit


def back_menu():
    clear_and_exit(controle_material)


controle_material.b_menu.clicked.connect(back_menu)
controle_material.setWindowFlag(Qt.FramelessWindowHint)
center_screen(controle_material)
