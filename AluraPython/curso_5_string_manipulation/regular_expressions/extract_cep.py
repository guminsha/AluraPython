import re # Regular Expressions -- RegEx (Lib default)

adress = "Rua Jornalista Augusto Vaz Filho 992, apartamento 404, Pinheiro, Maceió, AL, 57057-150"

pattern = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")
search = pattern.search(adress)

if search:
	cep = search.group()

print(cep)