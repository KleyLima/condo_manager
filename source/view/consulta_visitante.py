# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, consulta_visitante
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen



consulta_visitante.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(consulta_visitante)