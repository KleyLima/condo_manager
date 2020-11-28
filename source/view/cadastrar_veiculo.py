# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_veiculo
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu
from source.dao.models.visitante import Visitante
from source.dao.visitante_dao import select_by_name
from source.controller.veiculo_controller import validate

# inicializaçao da base de proprietarios no combo box.
di = {}
def load_base():

    lista_nome = select_by_name()

    for nome in lista_nome.select():
        di[nome.visitor_name] = nome.id
        cadastrar_veiculo.combo_proprietario.addItem(nome.visitor_name)


    cadastrar_veiculo.combo_proprietario.addItem("Ricardo")
    cadastrar_veiculo.combo_proprietario.addItem("Gustavo")
    cadastrar_veiculo.combo_proprietario.addItem("Brazza")
    cadastrar_veiculo.combo_proprietario.addItem("Kleyton")


def clear_and_exit():
    clear_input_boxes(cadastrar_veiculo)
    back_to_menu(cadastrar_veiculo)


def add_vehicle():
    print(di)
    nome_prop = di[cadastrar_veiculo.combo_proprietario.currentText()]
    placa = cadastrar_veiculo.line_placa_veiculo.text()
    cor = cadastrar_veiculo.line_cor_veiculo.text()
    if cadastrar_veiculo.tipo_moto.isChecked():
        tipo = "Moto"
    else:
        tipo = "Carro"

    if validate(nome_prop, placa, cor, tipo):
        clear_input_boxes(cadastrar_veiculo)
     
    



load_base()
cadastrar_veiculo.salvar_veiculo.clicked.connect(add_vehicle)
cadastrar_veiculo.cancel.clicked.connect(clear_and_exit)
cadastrar_veiculo.setWindowFlag(Qt.FramelessWindowHint)
cadastrar_veiculo.tipo_carro.setChecked(True)
center_screen(cadastrar_veiculo)



