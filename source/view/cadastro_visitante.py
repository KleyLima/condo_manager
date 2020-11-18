# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_visitante
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen

# Example of a funcion assigned to a button:
# form_visitante.salvar_visi.clicked.connect(teste)
cadastro_visitante.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(cadastro_visitante)
