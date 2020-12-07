# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_imovel
from PyQt5.QtCore import Qt
from source.dao.pessoa_dao import select_all
from source.controller.imovel_controller import validate
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu


di = {}
def load_base_imovel():

    di = {}
    lista_nome = select_all()

    for nome in lista_nome.select():
        di[nome.name] = nome.id
        cadastrar_imovel.combo_dono.addItem(nome.name)



def add_home():
    nome_prop = di[cadastrar_imovel.combo_dono.currentText()]
    number_home = cadastrar_imovel.line_num.text()
    
    if validate(nome_prop, number_home):
        load_base_imovel()
        clear_input_boxes(cadastrar_imovel)


def clear_and_exit():
    clear_input_boxes(cadastrar_imovel)
    back_to_menu(cadastrar_imovel)




load_base_imovel()
cadastrar_imovel.salvar_imovel.clicked.connect(add_home)
cadastrar_imovel.setWindowFlag(Qt.FramelessWindowHint)
cadastrar_imovel.cancel.clicked.connect(clear_and_exit)
center_screen(cadastrar_imovel)
