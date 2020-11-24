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
menu = Telas("/resource/telas/menu.ui").loaded
cadastro_visitante = Telas("/resource/telas/cadastro_visitante.ui").loaded   #
cadastro_locatario = Telas("/resource/telas/cadastro_locatario.ui").loaded   #
consulta_visitante = Telas("/resource/telas/consulta_visitante.ui").loaded   #
cadastro_locadores = Telas("/resource/telas/cadastro_locadores.ui").loaded   #
cadastrar_imovel = Telas("/resource/telas/cadastrar_imovel.ui").loaded       #
cadastrar_veiculo = Telas("/resource/telas/cadastrar_veiculo.ui").loaded     #
cadastrar_locacao = Telas("/resource/telas/cadastrar_locacao.ui").loaded     #
controle_material = Telas("/resource/telas/controle_material.ui").loaded
error = Telas("/resource/telas/error.ui").loaded
