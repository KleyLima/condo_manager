# -*- coding: utf-8 -*-


from source.dao.models.materiais import Materiais
from source.dao.visitante_dao import select_by_name



def insert_material(nome_produto, qtd):
    material = Materiais(
        product_name = nome_produto,
        product_qtd = qtd
    )
    print("Inserting new product...")
    return material.save()