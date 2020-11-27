# -*- coding: utf-8 -*-

from source.utils.validation_utils import email_checker
from source.dao.visitante_dao import insert_visitor
from source.utils.error_utils import plot_errors
from source.dao.visitante_dao import select_by_cpf


def validate(name, email, cpf, tel, address):
    # TODO: Create the error window/frame
    val_fields = valid_fields(name, email, cpf, tel, address)
    val_email = validate_email(email)
    print(val_fields, val_email)
    if val_fields:
        plot_errors(val_fields)
        return False
    if val_email:
        plot_errors(val_email)
        return False
    insert_visitor(name, email, cpf, tel, address)
    return True


def valid_fields(name, email, cpf, tel, address):
    print("Validating fields")
    err_msg = ""
    if not name:
        err_msg += "Name field cannot be blank.\n"
    if not cpf:
        err_msg += "CPF field cannot be blank.\n"
    if not tel:
        err_msg += "Telephone field cannot be blank."
    return False if not err_msg else err_msg


def validate_email(email):
    print("Validating email")
    if not email_checker(email):
        return "Email not valid."
    return False


def cpf_consulting(cpf):
    """
    Function that consulting the database looking for CPF.
    params: receive a CPF of the consulta_visitante.
    return: just a simple message.
    """

    cpf_ver = select_by_cpf(cpf)
    
    # if cpf_ver == "":
    #     msg = f'Campo em branco, favor digitar um CPF.'
    #     plot_errors(msg)
        
    if cpf_ver:
        msg = f'CPF cadastrado.'
        plot_errors(msg)
    else:
        msg = f'Campo em branco ou CPF inválido.'
        plot_errors(msg)
        

#TODO should be a main viwe for to messages.
def err_consulta(msg):
    plot_errors(msg)