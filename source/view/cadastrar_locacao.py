# -*- coding: utf-8 -*-

from source.dao.models.imovel import Imovel
from resource.telas.inicializacao import app, cadastrar_locacao
from PyQt5.QtCore import Qt
from source.controller.locacao_controller import validate
from source.dao.pessoa_dao import select_by_name_locador, select_by_name_locatario
from source.dao.imovel_dao import select_by_imovel
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu


# TODO Trocar pelo select de locadores
# to use index to add in database
di = {}
def load_locador():

    
    lista_nome = select_by_name_locador()

    for nome in lista_nome.select():
        di[nome.name] = nome.id
        cadastrar_locacao.combo_locador.addItem(nome.name)



# TODO Trocar pelo select de locatario
# to use index to add in database
di2 = {}
def load_locatario():

    
    lista_nome = select_by_name_locatario()

    for nome in lista_nome.select():
        di2[nome.name] = nome.id
        cadastrar_locacao.combo_locatario.addItem(nome.name)



# TODO Trocar pelo select de imovel
# to use index to add in database
di3 = {}
def load_imovel():

    
    lista_nome = select_by_imovel()

    for nome in lista_nome.select():
        di3[nome.name] = nome.id
        cadastrar_locacao.combo_imovel.addItem(nome.name)



# Create a contrato locador at database
def contrato_locacao():
    # Em casa de erro, verificar se está entregando o id so nome de acordo com a lista criada.
    nome_locador = di[cadastrar_locacao.combo_locador.currentText()]
    nome_locatario = di2[cadastrar_locacao.combo_locatario.currentText()]
    imovel = di3[cadastrar_locacao.combo_imovel.currentText()]
    data_inicio = cadastrar_locacao.line_dt_inicio.text()
    data_fim =  cadastrar_locacao.line_dt_fim.text()
    valor = cadastrar_locacao.line_aluguel.text()
    
    

    if validate(nome_locador, nome_locatario, imovel, data_inicio, data_fim, valor):
        clear_input_boxes(cadastrar_locacao)



def clear_and_exit():
    clear_input_boxes(cadastrar_locacao)
    back_to_menu(cadastrar_locacao)




cadastrar_locacao.salvar_locacao.clicked.connect(contrato_locacao)
cadastrar_locacao.setWindowFlag(Qt.FramelessWindowHint)
cadastrar_locacao.cancel.clicked.connect(clear_and_exit)
center_screen(cadastrar_locacao)
# Load bases
load_locador()
load_locatario()
load_imovel()