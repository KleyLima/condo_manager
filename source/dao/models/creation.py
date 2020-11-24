from source.dao.models.owner import Owner
from source.dao.models.address import Address
from source.dao.models.imovel import Imovel
from source.dao.models.locacao import Locacao
from source.dao.models.materiais import Materiais
from source.dao.models.pessoa import Pessoa
from source.dao.models.veiculo import Veiculo
from source.dao.models.visitante import Visitante

if __name__ == "__main__":
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

    try:
        Imovel.create_table()
        print("Tabela 'Imovel' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Imovel' ja existe!")

    try:
        Locacao.create_table()
        print("Tabela 'Locacao' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Locacao' ja existe!")

    try:
        Materiais.create_table()
        print("Tabela 'Materiais' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Materiais' ja existe!")

    try:
        Pessoa.create_table()
        print("Tabela 'Pessoa' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Pessoa' ja existe!")

    try:
        Veiculo.create_table()
        print("Tabela 'Veiculo' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Veiculo' ja existe!")

    try:
        Visitante.create_table()
        print("Tabela 'Visitante' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Visitante' ja existe!")
