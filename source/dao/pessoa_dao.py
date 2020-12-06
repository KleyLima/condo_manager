# -*- coding: utf-8 -*-

from source.dao.models.pessoa import Pessoa

# Inserting imovel at Database
def insert_pessoa(nome, email, cpf, nacio, fone, nasc, tipo, sexo):
    pessoa = Pessoa(
        name = nome,
        email = email,
        cpf = cpf,
        nacionality = nacio, 
        phone = fone,
        birthday = nasc,
        costumer_type = tipo,
        sex = sexo
    )
    print("Inserting new person...")
    return pessoa.save()



# Realiza a busca de todos os nomes de locadores somentes
def select_by_name_locador():
    by_name = Pessoa.select().where(Pessoa.name != "", Pessoa.costumer_type == "locador").get()
    return by_name


# Realiza a busca de todos os nomes de locatarios somente
def select_by_name_locatario():
    by_name = Pessoa.select().where(Pessoa.name != "", Pessoa.costumer_type == "locatario").get()
    return by_name