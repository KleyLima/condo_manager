from source.dao.models.db import BaseModel, peewee


class Imovel(BaseModel):
    """
    Representa base dos imoveis cadastrados
    """

    id_owner = peewee.IntegerField() # foreign key as filter  = locador
    home_number = peewee.IntegerField(null=False)