# -*- coding: utf-8 -*-

"""
    Orquestrador da aplicação.
"""

from PyQt5 import uic, QtWidgets
from source.view.menu import *
from os import environ
from source.view.cadastro_visitante import *
from source.view.cadastro_locatario import *
from source.view.controle_material import *
from source.view.consulta_visitante import *
from source.view.cadastro_locadores import *
from source.view.cadastrar_veiculo import *
from source.view.cadastrar_locacao import *
from source.view.cadastrar_imovel import *
from source.view.error import *


# inicialização da tela principal
menu.show()


app.exec()


