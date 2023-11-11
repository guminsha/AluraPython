class ExtractorURL:
	def __init__(self, url) -> None:
		self.url = self.clean_url(url)
		self.url_validation()

	def clean_url(self, url):
		if type(url) == str:
			return url.strip()
		else:
			return ""
	
	def url_validation(self):
		if not self.url:
			raise ValueError("URL is empty")
		
	def get_url_base(self):
		interrogation_index = self.url.find("?")
		url_base = self.url[:interrogation_index]
		return url_base

	def get_url_parameters(self):
		interrogation_index = self.url.find("?")
		url_parameters = self.url[interrogation_index+1:]
		return url_parameters

	def get_value_parameter(self, parameter):
		index_parameter = self.get_url_parameters().find(parameter)
		index_value = index_parameter + len(parameter)+1
		e_commerce_index = self.get_url_parameters().find("&", index_value)
		if e_commerce_index == -1:
			value = self.get_url_parameters()[index_value:]
		else: 
			value = self.get_url_parameters()[index_value:e_commerce_index]

		return value

extractor_url = ExtractorURL("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
extractor_url = ExtractorURL(None)
value_quantity = extractor_url.get_value_parameter("quantidade")
print(value_quantity)