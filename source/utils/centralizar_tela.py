# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDesktopWidget


def center_screen(tela):
    """
    Wanna a window centred on screen? here is your saviour!
    :param tela: Screen to be centred. Is a PyQt5 QtWidget object
    :return: None
    """
    screen = QDesktopWidget().screenGeometry()
    widget = tela.geometry()
    x = screen.width() - widget.width()
    y = screen.height() - widget.height()
    tela.move(x / 2, y / 2)
