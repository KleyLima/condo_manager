from source.dao.models.visitante import Visitante

"""
    This is the central os visitantes functions.
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


def select_by_cpf(cpf):
    by_cpf = Visitante.select().where(Visitante.visitor_cpf == cpf).limit(1)
    return True if len(by_cpf) > 0 else False
    # try:
    #     return True
    # except Visitante.model.DoesNotExist:
    #     return False
