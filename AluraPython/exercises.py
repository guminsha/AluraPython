usuario = input("Informe o usuário do sistema: ")
lista_convidados = ["Flavio", "Douglas", "Nico"]


for i in lista_convidados:
    print(lista_convidados)
    lista_convidados.append(i.lower())
    lista_convidados.remove(i)

if usuario.lower() in lista_convidados:
    print(f"Seja bem-vindo {usuario}!")
else:
    print("Usuário não identificado!")


