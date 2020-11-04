# -*- coding: utf-8 -*-

from resource.testes.telas import app, locador
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen

print("Teste")

locador.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(locador)