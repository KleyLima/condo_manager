for ent in ["Imovel",
            "Locacao",
            "Materiais",
            "Pessoa",
            "Veiculo",
            "Visitante"]:
    print("""
    try:
      {}.create_table()
      print("Tabela '{}' criada com sucesso!")
    except peewee.OperationalError:
      print("Tabela '{}' ja existe!")
      """.format(ent, ent, ent))
