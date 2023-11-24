import requests

class SearchAdress:
	def __init__(self, cep) -> None:
		cep = str(cep)
		if self.validation_cep(cep):
			self.cep = cep
		else:
			raise ValueError("Wrong number of digits")
		
		
	def validation_cep(self, cep):
		if len(cep) == 8:
			return True
		else:
			return False
		
	def format_cep(self):
		return f"{self.cep[:5]}-{self.cep[5:]}"
	
	def acess_viacep(self):
		url = f"https://viacep.com.br/ws/{self.cep}/json/"
		r = requests.get(url)
		data = r.json()
		
		return (data["bairro"], data["localidade"], data["uf"])

	def __str__(self) -> str:
		return self.format_cep()