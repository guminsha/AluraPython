from acess_cep import SearchAdress

adress1 = SearchAdress("01015100")

neighborhood, city, state = adress1.acess_viacep()
print(neighborhood, city, state)