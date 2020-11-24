# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_visitante, menu
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu
from PyQt5.QtWidgets import QLineEdit
from source.controller.visitante_controller import validate


def clear_and_exit():
    clear_input_boxes(cadastro_visitante)
    back_to_menu(cadastro_visitante)


def send():
    name = cadastro_visitante.line_nome_visitante.text()
    email = cadastro_visitante.line_email_visitante.text()
    cpf = cadastro_visitante.line_cpf_visitante.text()
    tel = cadastro_visitante.line_telef_visitante.text()
    address = cadastro_visitante.line_ender_visitante.text()
    if validate(name, email, cpf, tel, address):
        clear_input_boxes(cadastro_visitante)


cadastro_visitante.salvar_visitante.clicked.connect(send)
cadastro_visitante.cancel.clicked.connect(clear_and_exit)
cadastro_visitante.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastro_visitante)
