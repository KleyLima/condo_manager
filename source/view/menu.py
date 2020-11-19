# -*- coding: utf-8 -*-

from resource.telas.inicializacao import (
    app,
    menu,
    cadastro_visitante,
    cadastro_locatario,
    consulta_visitante,
    cadastro_locadores,
    cadastrar_imovel,
    cadastrar_veiculo,
    cadastrar_locacao,
    controle_material,
)
from time import sleep
from source.utils.centralizar_tela import center_screen


def b_consulta_visitante():
    menu.hide()
    consulta_visitante.show()


def b_cadastro_visitante():
    menu.hide()
    cadastro_visitante.show()


def b_cadastro_locatario():
    menu.hide()
    cadastro_locatario.show()


def b_cadastro_locador():
    menu.hide()
    cadastro_locadores.show()


def b_cadastrar_imovel():
    menu.hide()
    cadastrar_imovel.show()


def b_cadastrar_veiculo():
    menu.hide()
    cadastrar_veiculo.show()


def b_contrato_locacao():
    menu.hide()
    cadastrar_locacao.show()


def b_gerencias_materias():
    menu.hide()
    controle_material.show()


menu.b_consulta_visitante.clicked.connect(b_consulta_visitante)
menu.b_cadastro_visitante.clicked.connect(b_cadastro_visitante)
menu.b_cadastro_locador.clicked.connect(b_cadastro_locador)
menu.b_cadastro_locatario.clicked.connect(b_cadastro_locatario)
menu.b_cadastrar_imovel.clicked.connect(b_cadastrar_imovel)
menu.b_cadastrar_veiculo.clicked.connect(b_cadastrar_veiculo)
menu.b_gerencias_materias.clicked.connect(b_gerencias_materias)
menu.b_contrato_locacao.clicked.connect(b_contrato_locacao)
center_screen(menu)
