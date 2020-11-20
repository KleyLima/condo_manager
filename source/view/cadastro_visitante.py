# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_visitante, menu
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu
from PyQt5.QtWidgets import QLineEdit


def teste():
    clear_input_boxes(cadastro_visitante)
    back_to_menu(cadastro_visitante)


cadastro_visitante.cancel.clicked.connect(teste)
cadastro_visitante.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastro_visitante)
