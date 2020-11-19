from source.dao.models.db import BaseModel, peewee


class Veiculo(BaseModel):
    """
    Representa base de veiculos cadastrados das pessoas do condominio.
    """

    id_owner = peewee.IntegerField()  # Foreign key (locador ou locatario)
    license_plate = peewee.CharField(null=False)
    color = peewee.CharField(null=False)
    vehicle_type = peewee.CharField()
