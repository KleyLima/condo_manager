# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, consulta_visitante
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen


consulta_visitante.setWindowFlag(Qt.FramelessWindowHint)
center_screen(consulta_visitante)
