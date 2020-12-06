# -*- coding: utf-8 -*-

from source.dao.material_dao import insert_material
from source.utils.error_utils import plot_errors


def validate(nome_produto, qtd):
    # TODO: Create the error window/frame
    val_fields = valid_fields(nome_produto, qtd)

    if val_fields:
        plot_errors(val_fields)
        return False
    insert_material(nome_produto, qtd)
    return True


def valid_fields(nome_produto, qtd):
    print("Validating fields")
    err_msg = ""
    if not nome_produto:
        err_msg += "Name field cannot be blank.\n"
    if not qtd:
        err_msg += "Quantifier field cannot be blank.\n"
    return False if not err_msg else err_msg