# -*- coding: utf-8 -*-

"""
    Orquestrador da aplicação.
"""

from PyQt5 import uic, QtWidgets
from os import environ
from resource.testes.telas import *

def b_consulta_visitante():
    consulta_cli.show()

def b_cadastro_visitante():
    form_visitante.show()

def b_cadastro_locador():
    locador.show()

def b_cadastro_locatario():
    form_locatario.show()

# inicialização da tela principal
menu.b_consulta_visitante.clicked.connect(b_consulta_visitante)
menu.b_cadastro_visitante.clicked.connect(b_cadastro_visitante)
menu.b_cadastro_locador.clicked.connect(b_cadastro_locador)
menu.b_cadastro_locatario.clicked.connect(b_cadastro_locatario)
menu.show()





app.exec()