# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QLineEdit
from source.view.menu import menu


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


def clear_input_boxes(frame):
    """
    As the name suggests clear the text of all input boxes named as QLineEdit in Qt lib.
    Works only for input boxes, so combo boxes, lists will still hold the past values.
    :param frame: (QtWidget) A frame/window to be cleared.
    :return: None.
    """
    for input_box in frame.findChildren(QLineEdit):
        input_box.clear()


def back_to_menu(frame):
    """
    Hide the current frame and show the main menu of the application.
    :param frame: (QtWidget) A frame/window to be swaped for the menu
    :return: None.
    """
    frame.hide()
    menu.show()
