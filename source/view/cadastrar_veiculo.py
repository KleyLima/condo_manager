# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_veiculo
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen


cadastrar_veiculo.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(cadastrar_veiculo)