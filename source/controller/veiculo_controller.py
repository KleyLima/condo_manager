# -*- coding: utf-8 -*-

from source.dao.veiculo_dao import insert_veiculo
from source.utils.error_utils import plot_errors


def validate(nome_prop, placa, cor, tipo):
    # TODO: Create the error window/frame
    val_fields = valid_fields(nome_prop, placa, cor, tipo)
    print(val_fields)
    if val_fields:
        plot_errors(val_fields)
        return False
    insert_veiculo(nome_prop, placa, cor, tipo)
    return True


def valid_fields(nome_prop, placa, cor, tipo):
    print("Validating fields")
    err_msg = ""
    if not nome_prop:
        err_msg += "Name field cannot be blank.\n"
    if not placa:
        err_msg += "Placa field cannot be blank.\n"
    if not cor:
        err_msg += "Color field cannot be blank."
    if not tipo:
        err_msg += "Type not specified."
    return False if not err_msg else err_msg