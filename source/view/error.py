# -*- coding: utf-8 -*-

from resource.telas.inicializacao import app, error
from PyQt5.QtCore import Qt
from source.utils.screen_utils import center_screen, back_to_menu, clear_input_boxes


print(type(error))


def exit():
    print(type(error))
    # clear_input_boxes(error)
    error.list_errors.clear()
    error.hide()


center_screen(error)
error.okay.clicked.connect(exit)
# flags = Qt.WindowFlags()
# error.setWindowFlags(Qt.WindowCloseButtonHint)
