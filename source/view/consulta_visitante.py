# -*- coding: utf-8 -*-

from source.utils.error_utils import plot_errors
from resource.telas.inicializacao import app, consulta_visitante
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen

from source.controller.visitante_controller import err_consulta,cpf_consulting


def consultar_cpf():
    cpf = consulta_visitante.line_cpf.text()
    cpf_consulting(cpf)
    
        

def clear_and_exit():
    clear_input_boxes(consulta_visitante)
    back_to_menu(consulta_visitante)




consulta_visitante.consultar_visitante.clicked.connect(consultar_cpf)
consulta_visitante.cancel.clicked.connect(clear_and_exit)
consulta_visitante.setWindowFlag(Qt.FramelessWindowHint)
center_screen(consulta_visitante)

