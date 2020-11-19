from source.dao.models.address import Address


def insert_address(address, number, cep, complement, state, city, neighborhood):
    addr = Address(
        address=address,
        number=number,
        cep=cep,
        complement=complement,
        state=state,
        city=city,
        neighborhood=neighborhood,
    )
    return addr.save()


def delete_address(address, number, cep, complement, state, city, neighborhood):
    pass


def select_by_address(address):
    return Address.select(Address.cep).where(Address.address == address).get()


if __name__ == "__main__":
    # insert_address("Rua CAntareira", 123, "789465-12", "Bloco 4", "SP", "OZ", "OZ")
    # print("Created")
    print(vars(select_by_address("Rua CAntareira")))
