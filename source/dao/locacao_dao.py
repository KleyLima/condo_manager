# -*- coding: utf-8 -*-

from source.dao.models.locacao import Locacao
from source.dao.visitante_dao import select_by_name


# Inserting imovel at Database
def insert_locacao(id_locador, id_locatario, id_imovel, initial_date, finish_date, rented_value):
    locacao = Locacao(
        id_locador = id_locador,
        id_locatario = id_locatario,
        id_imovel = id_imovel,
        initial_date = initial_date,
        finish_date = finish_date, 
        rented_value = rented_value
    )
    print("Inserting new locacao...")
    return locacao.save()