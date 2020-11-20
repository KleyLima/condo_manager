# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, cadastrar_locacao
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen


cadastrar_locacao.setWindowFlag(Qt.FramelessWindowHint)
center_screen(cadastrar_locacao)
