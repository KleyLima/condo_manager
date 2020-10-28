from source.dao.models.owner import Owner
from source.dao.models.address import Address

if __name__ == '__main__':
    try:
        Owner.create_table()
        print("Tabela 'Owner' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Owner' ja existe!")

    try:
        Address.create_table()
        print("Tabela 'Address' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Address' ja existe!")
