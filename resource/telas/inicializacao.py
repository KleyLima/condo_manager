# -*- coding: utf-8 -*-

"""
    Classe central de telas: inicialçização e carregamento das telas do App
"""
from os import environ
from PyQt5 import uic, QtWidgets

source_interface = environ.get("PYTHONPATH")


class Telas:
    def __init__(self, path):
        self.path = path
        self.loaded = None
        self.load()

    def load(self):
        self.loaded = uic.loadUi(source_interface + self.path)

    def show(self):
        if not self.loaded:
            self.load()

        self.loaded.show()

    def hide(self):
        self.loaded.hide()


app = QtWidgets.QApplication([])
# primeira_tela = Telas("/resource/telas/untitled.ui").loaded
# locador = Telas("/resource/telas/form_locador.ui").loaded
# endereco = Telas("/resource/telas/form_ender.ui").loaded
menu = Telas("/resource/telas/menu.ui").loaded
# consulta_visitante = Telas("/resource/telas/form_consulta_cli.ui").loaded
cadastro_visitante = Telas("/resource/telas/cadastro_visitante.ui").loaded
cadastro_locatario = Telas("/resource/telas/cadastro_locatario.ui").loaded