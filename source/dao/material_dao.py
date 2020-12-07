# -*- coding: utf-8 -*-


from source.dao.models.materiais import Materiais


def insert_material(nome_produto, qtd):
    material = Materiais(
        product_name = nome_produto,
        product_qtd = qtd
    )
    print("Inserting new product...")
    return material.save()


# Realiza a busca de todos os nomes de locadores somentes
def select_by_material():
    by_name = Materiais.select().where(Materiais.product_name != "").get()
    return by_name


def update_add_material(produto, qtd):
    upd = Materiais.update(product_qtd= Materiais.product_qtd + qtd).where(Materiais.product_name == produto)
    return upd

def update_rem_material(produto, qtd):
    upd = Materiais.update(product_qtd= Materiais.product_qtd - qtd).where(Materiais.product_name == produto)
    return upd


def select_all():
    by_name = Materiais.select().where(Materiais.product_name != "")
    return by_name



# if __name__ == '__main__':

#     """
#         Caso queira testar os valores dos itens apos update ou remove.
#     """
#     lista = select_all()
#     print(lista)

#     for qtd in lista:
#         print(qtd.product_qtd)