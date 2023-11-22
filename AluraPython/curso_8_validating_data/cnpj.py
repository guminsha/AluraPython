from validate_docbr import CNPJ

class Cnpj:
	def __init__(self, doc) -> None:
		if self.valid_cnpj(doc):
			self.cnpj = doc
		else:
			raise ValueError("Invalid CNPJ")

	def valid_cnpj(self, doc):
		if len(doc) == 14:
			validating = CNPJ()
			return validating.validate(doc)
		else:
			raise ValueError("Wrong number of digits")
		
	def format_cnpj(self):
		formated_cnpj = CNPJ().mask(self.cnpj)
		return formated_cnpj

	def __str__(self) -> str:
		return self.format_cnpj()
