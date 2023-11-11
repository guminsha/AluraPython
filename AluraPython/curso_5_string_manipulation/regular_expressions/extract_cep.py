import re # Regular Expressions -- RegEx (Lib default)

adress = "Rua Jornalista Augusto Vaz Filho 992, apartamento 404, Pinheiro, Maceió, AL, 57057-150"

pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") # [Digits]{quantity} {0,1 = 0 or 1 times}
search = pattern.search(adress)

if search:
	cep = search.group()

print(cep)