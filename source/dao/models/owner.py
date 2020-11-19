from source.dao.models.db import BaseModel, peewee
from source.dao.models.address import Address


class Owner(BaseModel):
    """
    Classe que representa um proprietário de imóvel dentro da aplicação
    """

    owner_name = peewee.CharField()
    cpf = peewee.CharField()
    email = peewee.CharField()
    telephone = peewee.CharField()
    sex = peewee.CharField()
    birthday = peewee.DateField()
    nationality = peewee.CharField(null=True)
    type_person = peewee.CharField()
    address = peewee.ForeignKeyField(Address)
