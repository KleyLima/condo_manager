# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_imovel
from PyQt5.QtCore import Qt
from source.dao.visitante_dao import select_by_name
from source.dao.models.visitante import Visitante
from source.controller.imovel_controller import validate
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu


di = {}
def load_base():

    lista_nome = select_by_name()

    for nome in lista_nome.select():
        di[nome.visitor_name] = nome.id
        cadastrar_imovel.combo_dono.addItem(nome.visitor_name)


    cadastrar_imovel.combo_dono.addItem("Ricardo")
    cadastrar_imovel.combo_dono.addItem("Gustavo")
    cadastrar_imovel.combo_dono.addItem("Brazza")
    cadastrar_imovel.combo_dono.addItem("Kleyton")


def add_home():
    nome_prop = di[cadastrar_imovel.combo_dono.currentText()]
    number_home = cadastrar_imovel.line_num.text()
    
    if validate(nome_prop, number_home):
        clear_input_boxes(cadastrar_imovel)


def clear_and_exit():
    clear_input_boxes(cadastrar_imovel)
    back_to_menu(cadastrar_imovel)


load_base()
cadastrar_imovel.salvar_imovel.clicked.connect(add_home)
cadastrar_imovel.setWindowFlag(Qt.FramelessWindowHint)
cadastrar_imovel.cancel.clicked.connect(clear_and_exit)
center_screen(cadastrar_imovel)
