from source.dao.models.db import BaseModel, peewee


class Locacao(BaseModel):
    """
    Representa base de dados sobre a locação do imovel
    teremos 3 chaves estrangeiras: locador, locatario, imovel
    """

    id_locador = peewee.IntegerField() # foreign key 
    id_locatario = peewee.IntegerField() # foreign key 
    id_imovel = peewee.IntegerField()  # foreign key 
    initial_date = peewee.CharField(null=False)
    finish_date = peewee.CharField(null=False)
    rented_value = peewee.DoubleField(null=False)
