import peewee
from os import environ


base = environ.get("PYTHONPATH") + "/source/dao/models/"
db = peewee.SqliteDatabase(base + 'test_condo.db')


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente
        database = db
