# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_locatario
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen


# form_locatario.salvar_owner.clicked.connect()
cadastro_locatario.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(cadastro_locatario)
