# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_locadores
from PyQt5.QtCore import Qt
from source.controller.pessoa_controller import validate
from source.utils.screen_utils import center_screen, clear_input_boxes, back_to_menu
from source.view.cadastrar_veiculo import load_base
from source.view.cadastrar_imovel import load_base_imovel
from source.view.cadastrar_locacao import load_locador, load_locatario, load_imovel



def add_locadores():
    nome = cadastro_locadores.line_nome_locador.text()
    email = cadastro_locadores.line_email_locador.text()
    cpf = cadastro_locadores.line_cpf_locador.text()
    nacio = cadastro_locadores.line_nacio_locador.text()
    tel = cadastro_locadores.line_telef_locador.text()
    nasc = cadastro_locadores.line_nasc_locador.text()

    if cadastro_locadores.tipo_locador.isChecked():
        tipo = "locador"


    if cadastro_locadores.rb_masc.isChecked():
        sexo = "masculino"
    elif cadastro_locadores.rb_fem.isChecked():
        sexo = "feminino"
    elif cadastro_locadores.rb_outros.isChecked():
        sexo = "outros"


    if validate(nome, email, cpf, nacio, tel, nasc, tipo, sexo):
        load_base()
        load_base_imovel()
        load_locador()
        load_locatario()
        load_imovel()
        clear_input_boxes(cadastro_locadores)



def clear_and_exit():
    clear_input_boxes(cadastro_locadores)
    back_to_menu(cadastro_locadores)




cadastro_locadores.salvar_locador.clicked.connect(add_locadores)
cadastro_locadores.setWindowFlag(Qt.FramelessWindowHint)
cadastro_locadores.cancel.clicked.connect(clear_and_exit)
cadastro_locadores.rb_masc.setChecked(True)
cadastro_locadores.tipo_locador.setChecked(True)
cadastro_locadores.tipo_locatario.setDisabled(True)
center_screen(cadastro_locadores)
