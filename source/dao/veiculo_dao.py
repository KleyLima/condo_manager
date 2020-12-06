# -*- coding: utf-8 -*-


from source.dao.models.veiculo import Veiculo
from source.dao.models.visitante import Visitante
from source.dao.visitante_dao import select_by_name



def insert_veiculo(prop, placa, cor, tipo):
    veiculo = Veiculo(
        id_owner = prop,
        license_plate = placa,
        color = cor,
        vehicle_type = tipo
    )
    print("Inserting new vehicle...")
    return veiculo.save()
