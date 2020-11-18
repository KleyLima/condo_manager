# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, menu, cadastro_visitante, cadastro_locatario
from time import sleep


# def b_consulta_visitante():
#     b_consulta_visitante.show()


def b_cadastro_visitante():
    menu.hide()
    cadastro_visitante.show()


def b_cadastro_locatario():
    menu.hide()
    cadastro_locatario.show()


# menu.b_consulta_visitante.clicked.connect(b_consulta_visitante)
menu.b_cadastro_visitante.clicked.connect(b_cadastro_visitante)
# menu.b_cadastro_locador.clicked.connect(b_cadastro_locador)
menu.b_cadastro_locatario.clicked.connect(b_cadastro_locatario)
