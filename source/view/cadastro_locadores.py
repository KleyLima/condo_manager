# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastro_locadores
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import center_screen


cadastro_locadores.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastro_locadores)
