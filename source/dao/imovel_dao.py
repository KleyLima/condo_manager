# -*- coding: utf-8 -*-


from source.dao.models.imovel import Imovel
from source.dao.models.pessoa import Pessoa
from source.dao.visitante_dao import select_by_name


# Inserting imovel at Database
def insert_imovel(dono, number):
    imovel = Imovel(
        id_owner = dono,
        home_number = number,
    )
    print("Inserting new house...")
    return imovel.save()


# Realiza a busca de todos os nomes tanto locador ou locatario, para cadastrar um imovel.
def select_by_imovel():
    by_name = Pessoa.select().where(Pessoa.name != "").get()
    return by_name