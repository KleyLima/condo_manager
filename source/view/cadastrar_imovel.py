# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_imovel
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen


cadastrar_imovel.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(cadastrar_imovel)