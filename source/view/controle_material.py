# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, controle_material, menu, adicionar_material, cadastrar_material, deletar_material
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, clear_and_exit
from PyQt5.QtWidgets import QTableWidgetItem
from source.dao.material_dao import select_all


def cadastro_material():
    cadastrar_material.show()


def add_material():
    adicionar_material.show()


def rem_material():
    deletar_material.show()


def back_menu():
    clear_and_exit(controle_material)


def att_list():
    all_mat = select_all()
    controle_material.list_material.setColumnCount(3)
    controle_material.list_material.setHorizontalHeaderLabels(('Id', 'Nome', 'Qtd.'))
    controle_material.list_material.setRowCount(len(all_mat))
    for index, material in enumerate(all_mat):
        temp = QTableWidgetItem(str(material.id))
        controle_material.list_material.setItem(index, 0, temp)
        temp = QTableWidgetItem(material.product_name)
        controle_material.list_material.setItem(index, 1, temp)
        temp = QTableWidgetItem(str(material.product_qtd))
        controle_material.list_material.setItem(index, 2, temp)


controle_material.b_novo_produto.clicked.connect(cadastro_material)
controle_material.b_add_produto.clicked.connect(add_material)
controle_material.b_retirar_produto.clicked.connect(rem_material)
controle_material.b_menu.clicked.connect(back_menu)
controle_material.setWindowFlag(Qt.FramelessWindowHint)
center_screen(controle_material)
att_list()
