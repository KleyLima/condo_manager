# -*- coding: utf-8 -*-


from resource.testes.telas import app, form_locatario
from PyQt5.QtCore import Qt
from source.utils.centralizar_tela import location_on_the_screen


# form_locatario.salvar_owner.clicked.connect()
form_locatario.setWindowFlag(Qt.FramelessWindowHint)
location_on_the_screen(form_locatario)
