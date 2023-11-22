import re
from validate_docbr import CPF
#from document import Document

class Cpf:
	def __init__(self, doc) -> None:
		if self.valid_cpf(doc):
			self.cpf = doc
		else:
			raise ValueError("Invalid CPF")
	
	def valid_cpf(self, doc):
		# cpf_pattern = re.compile("\d{3}.\d{3}.\d{3}-\d{2}")
		# match = cpf_pattern.match(doc)
		
		if len(doc) == 11:
			validating = CPF()
			return validating.validate(doc)
		else:
			raise ValueError("Wrong number of digits")

	def format_cpf(self):
		# cpf_part1 = self.cpf[:3]
		# cpf_part2 = self.cpf[3:6]
		# cpf_part3 = self.cpf[6:9]
		# cpf_part4 = self.cpf[9:]
		# formated_cpf = f"{cpf_part1}.{cpf_part2}.{cpf_part3}-{cpf_part4}"

		formated_cpf = CPF().mask(self.cpf)

		return formated_cpf

	def __str__(self) -> str:
		return self.format_cpf()
