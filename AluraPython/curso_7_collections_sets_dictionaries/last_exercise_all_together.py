# testing the use of varios collections

from collections import Counter

def analyze_frequency(text):
	print("########## Starting analyzes ##########")
	text_counter = Counter(text.lower())
	total_characters_text = sum(text_counter.values())
	frequency = [(character, quantity / total_characters_text) for character, quantity in text_counter.items()]
	frequency = Counter(dict(frequency))
	for character, quantity in frequency.most_common(10):
		print(f"Char: {character} Percentage: {quantity * 100:.2f}%")

text1 = """
Saudacoes aventureiros,
A partir de 20 de novembro de 2023 (seg.), a politica do Steam impedira que sua loja aceite o peso argentino e outras moedas como forma de pagamento.
Como parte da atualizacao, havera alteracoes de precos nas compras de pacotes disponiveis para Black Desert SA na Steam Store.
"""

text2 = """
Saudacoes aventureiros,
As recompensas semanais do Santuario Obscuro Subjugacao de Chefes estao programadas para serem atualizadas durante a manutencao de 22 de novembro (qua.).
Portanto, as recompensas de Subjugacao de Chefes de 12 de novembro de 2023 (dom.) a 18 de novembro de 2023 (sab.) estao atualmente indisponiveis para coleta. 
Voce podera coleta-los apos a manutencao de 22 de novembro de 2023 (qua.). 
Por favor, confira abaixo para mais detalhes.  
"""

analyze_frequency(text1)
analyze_frequency(text2)


# text1_counter = Counter(text1.lower())
# total_characters_text1 = sum(text1_counter.values())
# text2_counter = Counter(text2.lower())
# total_characters_text2 = sum(text2_counter.values())

# # print(text1_counter)
# # print(total_characters_text1)
# # print(text2_counter)
# # print(total_characters_text2)

# for character, quantity in text1_counter.items():
# 	percentage = round(quantity/total_characters_text1 * 100, 2)
# 	tuple_caracters = (character, percentage)
# 	#print(f"Char: {character} appers {quantity} times of {total_characters_text1} it means {percentage}%")
# 	#print(f">>>>>>{tuple_caracters}<<<<<<")

# frequency = [(character, quantity / total_characters_text1)for character, quantity in text1_counter.items()]
# frequency = Counter(dict(frequency))
# print(frequency.most_common(10))
