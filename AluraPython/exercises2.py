# inteiros = [1,3,4,5,7,8,9]
# pares = [i for i in inteiros if i % 2 == 0]
# print(pares)

# ----------------------------

file = open("AluraPython\\teste.txt", "r")
# file.write("Banana\n")
# file.write("Maca\n")
# file.write("Uva\n")

conteudo = file.read()
print(conteudo)
conteudo = file.read()
print(conteudo)


file.close()