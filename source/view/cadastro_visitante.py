# -*- coding: utf-8 -*-

from resource.testes.telas import app, form_visitante
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen

# Example of a funcion assigned to a button:
# form_visitante.salvar_visi.clicked.connect(teste)
form_visitante.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(form_visitante)
