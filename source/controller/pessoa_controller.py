# -*- coding: utf-8 -*-

from source.dao.pessoa_dao import insert_pessoa
from source.utils.error_utils import plot_errors


def validate(nome, email, cpf, nacio, fone, nasc, tipo, sexo):
    # TODO: Create the error window/frame
    val_fields = valid_fields(nome, email, cpf, fone, nasc)

    if val_fields:
        plot_errors(val_fields)
        return False
    insert_pessoa(nome, email, cpf, nacio, fone, nasc, tipo, sexo)
    return True


def valid_fields(nome, email, cpf, fone, nasc):
    print("Validating fields")
    err_msg = ""
    if not nome:
        err_msg += "Name cannot be blank.\n"
    if not email:
        err_msg += " Email field cannot be blank.\n"
    if not cpf:
        err_msg += "CPF field cannot be blank.\n"
    if not fone:
        err_msg += "Phone field cannot be blank.\n"
    if not nasc:
        err_msg += "Birthday cannot be blank.\n"
    return False if not err_msg else err_msg