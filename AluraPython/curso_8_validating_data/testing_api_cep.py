from acess_cep import SearchAdress

adress1 = SearchAdress("01015100")

bairro, cidade, uf = adress1.acess_viacep()
print(bairro, cidade, uf)