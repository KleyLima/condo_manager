# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_locatario
from PyQt5.QtCore import Qt
from source.controller.pessoa_controller import validate
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu



def add_locatarios():
    nome = cadastro_locatario.line_nome_locatario.text()
    email = cadastro_locatario.line_email_locatario.text()
    cpf = cadastro_locatario.line_cpf_locatario.text()
    nacio = cadastro_locatario.line_nacio_locatario.text()
    tel = cadastro_locatario.line_telef_locatario.text()
    nasc = cadastro_locatario.line_nasc_locatario.text()
   
    
    if cadastro_locatario.tipo_locador.isChecked():
        tipo = "locador"
    else:
        tipo = "locatario"


    if cadastro_locatario.rb_masc.isChecked():
        sexo = "masculino"
    elif cadastro_locatario.rb_fem.click():
        sexo = "feminino"
    else:
        sexo = "outros"


    if validate(nome, email, cpf, nacio, tel, nasc, tipo, sexo):
        clear_input_boxes(cadastro_locatario)



def clear_and_exit():
    clear_input_boxes(cadastro_locatario)
    back_to_menu(cadastro_locatario)




# form_locatario.salvar_owner.clicked.connect()
cadastro_locatario.salvar_locatario.clicked.connect(add_locatarios)
cadastro_locatario.setWindowFlag(Qt.FramelessWindowHint)
cadastro_locatario.cancel.clicked.connect(clear_and_exit)
center_screen(cadastro_locatario)
