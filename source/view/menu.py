# -*- coding: utf-8 -*-

from resource.testes.telas import app, menu, consulta_cli, form_visitante, locador, form_locatario
from time import sleep


def b_consulta_visitante():
    consulta_cli.show()


def b_cadastro_visitante():
    menu.hide()
    form_visitante.show()


def b_cadastro_locador():
    locador.show()


def b_cadastro_locatario():
    form_locatario.show()


menu.b_consulta_visitante.clicked.connect(b_consulta_visitante)
menu.b_cadastro_visitante.clicked.connect(b_cadastro_visitante)
menu.b_cadastro_locador.clicked.connect(b_cadastro_locador)
menu.b_cadastro_locatario.clicked.connect(b_cadastro_locatario)
print(type(menu))
