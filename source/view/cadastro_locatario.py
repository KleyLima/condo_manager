# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_locatario
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen


# form_locatario.salvar_owner.clicked.connect()
cadastro_locatario.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastro_locatario)
