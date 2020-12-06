from resource.telas.inicializacao import app, controle_material, menu, adicionar_material, cadastrar_material, deletar_material
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit
from source.controller.material_controller import validate
from source.dao.material_dao import select_by_material
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu

# inicializaçao da base de proprietarios no combo box.
di = {}
def load_combo_add():

    lista_nome = select_by_material()

    for nome in lista_nome.select():
        di[nome.product_name] = nome.id
        adicionar_material.combo_materiais.addItem(nome.product_name)


di2 = {}
def load_combo_rem():

    lista_nome = select_by_material()

    for nome in lista_nome.select():
        di2[nome.product_name] = nome.id
        deletar_material.combo_materiais.addItem(nome.product_name)


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
        clear_and_exit(cadastrar_material)
     

# Function that do a update in database, adding qtd in a product list
def add_material():
    pass

# Function that do a update in database, removing qtd in a product list
def rem_material():
    pass





# Function buttons and more
cadastrar_material.cadastrar_material.clicked.connect(cadas_material)
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