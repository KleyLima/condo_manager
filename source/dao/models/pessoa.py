from source.dao.models.db import BaseModel, peewee


class Pessoa(BaseModel):
    """
    Representa base de pessoas independente se é locatario ou locador
    """

    name = peewee.CharField(null=False)
    email = peewee.CharField()
    cpf = peewee.CharField(null=False)
    nacionality = peewee.CharField()
    phone = peewee.CharField(null=False)
    birthday = peewee.CharField()
    costumer_type = peewee.CharField()
    sex = peewee.CharField()
