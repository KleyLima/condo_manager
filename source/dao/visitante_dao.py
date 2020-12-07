from source.dao.models.visitante import Visitante

"""
    This is the central os visitantes querys.
"""

def insert_visitor(name, email, cpf, tel, address):
    visi = Visitante(
        visitor_name=name,
        visitor_email=email,
        visitor_cpf=cpf,
        visitor_phone=tel,
        visitor_address=address
    )
    print("Inserting new visitor...")
    return visi.save()


# Retunn the unique cpf of the list.
def select_by_cpf(cpf):
    by_cpf = Visitante.select().where(Visitante.visitor_cpf == cpf).limit(1)
    return True if len(by_cpf) > 0 else False


def select_visitor_by_cpf(cpf):
    by_cpf = Visitante.select().where(Visitante.visitor_cpf == cpf).limit(1)
    return by_cpf

# Realiza a busca de todos os nomes de visitantes
def select_by_name():
    by_name = Visitante.select().where(Visitante.visitor_name != "").get()
    return by_name