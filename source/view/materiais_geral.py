from resource.telas.inicializacao import app, controle_material, menu, adicionar_material, cadastrar_material, deletar_material
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from source.controller.material_controller import validate
from source.dao.material_dao import select_by_material, update_add_material, update_rem_material
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu
from source.view.controle_material import att_list


# inicializaçao da base de produtos no combo box de adicionar.
di = {}


def load_combo_add():

    lista_nome = select_by_material()

    for nome in lista_nome.select():
        di[nome.product_name] = nome.id
        adicionar_material.combo_materiais.addItem(nome.product_name)


# inicializaçao da base de produtos no combo box de remover.
di2 = {}


def load_combo_rem():

    lista_nome = select_by_material()

    for nome in lista_nome.select():
        di2[nome.product_name] = nome.id
        deletar_material.combo_materiais.addItem(nome.product_name)


# Limpeza de cx de texto e retorno para pagina de controle de materiais
def clear_and_exit(frame):

    inputs = frame.findChildren(QLineEdit)
    if not isinstance(inputs, list):
        return False
    for input_box in inputs:
        input_box.clear()

    frame.hide()

    controle_material.show()


def back_cadasMaterial():
    clear_and_exit(cadastrar_material)


def back_addMaterial():
    clear_and_exit(adicionar_material)


def back_remMaterial():
    clear_and_exit(deletar_material)


# Function to register a product in database
def cadas_material():
    nome_produto = cadastrar_material.line_nome_material.text()
    qtd = cadastrar_material.line_qtd_material.text()

    if validate(nome_produto, qtd):
        load_combo_add()
        load_combo_rem()
        clear_and_exit(cadastrar_material)
        att_list()


# Function that do a update in database, adding qtd in a product list
def add_material():
    produto = adicionar_material.combo_materiais.currentText()
    qtd = adicionar_material.line_qtd_material.text()

    upd = update_add_material(produto, int(qtd))
    upd.execute()
    print("update complete...")

    clear_and_exit(adicionar_material)
    att_list()


# Function that do a update in database, removing qtd in a product list
def rem_material():

    produto = deletar_material.combo_materiais.currentText()
    qtd = deletar_material.line_qtd_material.text()

    upd = update_rem_material(produto, int(qtd))
    upd.execute()
    print("update complete...")

    clear_and_exit(deletar_material)
    att_list()


# Function buttons and more
cadastrar_material.cadastrar_material.clicked.connect(cadas_material)
adicionar_material.add_material.clicked.connect(add_material)
deletar_material.del_material.clicked.connect(rem_material)
cadastrar_material.cancel.clicked.connect(back_cadasMaterial)
adicionar_material.cancel.clicked.connect(back_addMaterial)
deletar_material.cancel.clicked.connect(back_remMaterial)
cadastrar_material.setWindowFlag(Qt.FramelessWindowHint)
adicionar_material.setWindowFlag(Qt.FramelessWindowHint)
deletar_material.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastrar_material)
center_screen(adicionar_material)
center_screen(deletar_material)
load_combo_add()
load_combo_rem()
