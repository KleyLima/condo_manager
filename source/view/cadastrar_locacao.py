# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_locacao
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen


cadastrar_locacao.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(cadastrar_locacao)