from source.dao.models.db import BaseModel, peewee


class Visitante(BaseModel):
    """
    Representa base de visitantes cadastrados
    """

    visitor_name = peewee.CharField(null=False)
    visitor_email = peewee.CharField()
    visitor_cpf = peewee.CharField(null=False)
    visitor_phone = peewee.CharField(null=False)
    visitor_address = peewee.CharField()
