# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, controle_material
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen


controle_material.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(controle_material)