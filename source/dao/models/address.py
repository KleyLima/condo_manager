from source.dao.models.db import BaseModel, peewee


class Address(BaseModel):
    """
    Representa um endereço, seja de imóvel, proprietário ou locatário na aplicação.
    """
    address = peewee.CharField()
    number = peewee.IntegerField()
    cep = peewee.CharField()
    complement = peewee.CharField(null=True)
    state = peewee.CharField()
    city = peewee.CharField()
    neighborhood = peewee.CharField()
