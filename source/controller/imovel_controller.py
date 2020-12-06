# -*- coding: utf-8 -*-

from source.dao.imovel_dao import insert_imovel
from source.utils.error_utils import plot_errors


def validate(nome_prop, number_home):
    # TODO: Create the error window/frame
    val_fields = valid_fields(nome_prop, number_home)

    if val_fields:
        plot_errors(val_fields)
        return False
    insert_imovel(nome_prop, number_home)
    return True


def valid_fields(nome_prop, number_home):
    print("Validating fields")
    err_msg = ""
    if not nome_prop:
        err_msg += "Name field cannot be blank.\n"
    if not number_home:
        err_msg += "Number house field cannot be blank.\n"
    return False if not err_msg else err_msg