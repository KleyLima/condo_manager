from source.dao.models.visitante import Visitante


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
    return Visitante.select().where(Visitante.visitor_cpf == cpf).get().visitor_name
