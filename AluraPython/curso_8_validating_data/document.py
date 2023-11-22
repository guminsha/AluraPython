from cpf import Cpf
from cnpj import Cnpj

class Document:
	@staticmethod
	def create_doc(document):
		if len(document) == 11:
			return Cpf(document)
		elif len(document) == 14:
			return Cnpj(document)
		else:
			raise ValueError("Wrong number of digits")