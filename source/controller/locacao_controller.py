# -*- coding: utf-8 -*-

from source.dao.locacao_dao import insert_locacao
from source.utils.error_utils import plot_errors


def validate(nome_locador, nome_locatario, imovel, data_inicio, data_fim, valor):
    # TODO: Create the error window/frame
    val_fields = valid_fields(nome_locador, nome_locatario, imovel, data_inicio, data_fim, valor)

    if val_fields:
        plot_errors(val_fields)
        return False
    insert_locacao(nome_locador, nome_locatario, imovel, data_inicio, data_fim, valor)
    return True


def valid_fields(nome_locador, nome_locatario, imovel, data_inicio, data_fim, valor):
    print("Validating fields")
    err_msg = ""
    if not nome_locador:
        err_msg += "Name locador cannot be blank.\n"
    if not nome_locatario:
        err_msg += "Name locatario field cannot be blank.\n"
    if not imovel:
        err_msg += "House field cannot be blank.\n"
    if not data_inicio:
        err_msg += "Initial date cannot be blank.\n"
    if not data_fim:
        err_msg += "Finish date cannot be blank.\n"
    if not valor:
        err_msg += "Rented value cannot be blank.\n"
    return False if not err_msg else err_msg