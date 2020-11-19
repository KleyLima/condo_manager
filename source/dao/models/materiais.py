from source.dao.models.db import BaseModel, peewee


class Materiais(BaseModel):
    """
    Representa base de estoque de materias do condominio
    """

    product_name = peewee.CharField(null=False)
    product_qtd = peewee.IntegerField(default=0)
