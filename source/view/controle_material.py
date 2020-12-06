# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, controle_material, menu, adicionar_material, cadastrar_material, deletar_material
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, clear_and_exit


def cadastro_material():
    cadastrar_material.show()
    


def add_material():
    adicionar_material.show()


def rem_material():
    deletar_material.show()



def back_menu():
    clear_and_exit(controle_material)





controle_material.b_novo_produto.clicked.connect(cadastro_material)
controle_material.b_add_produto.clicked.connect(add_material)
controle_material.b_retirar_produto.clicked.connect(rem_material)
controle_material.b_menu.clicked.connect(back_menu)
controle_material.setWindowFlag(Qt.FramelessWindowHint)
center_screen(controle_material)
