import re

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
		
		url_pattern = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
		match = url_pattern.match(self.url)

		if not match:
			raise ValueError("Invalid URL")
				
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
	
	def calculate_conversion(self):
		origin = self.get_value_parameter("moedaOrigem")
		destiny = self.get_value_parameter("moedaDestino")
		quantity = int(self.get_value_parameter("quantidade"))
		
		if origin == "dolar":
			final_value = quantity * 5.5
		elif origin == "real":
			final_value = quantity / 5.5
		else:
			print("Invalid currency")
		
		return final_value
	
	def __len__(self):
		return len(self.url)
	
	def __str__(self) -> str:
		return f"URL: {self.url}\nBase: {self.get_url_base()}\nParameters: {self.get_url_parameters()}"
	
	def __eq__(self, other) -> bool:
		return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extractor_url = ExtractorURL(url)

print(extractor_url.calculate_conversion())
	

# extractor_url2 = ExtractorURL(url)

# print(id(extractor_url)) # View memory adress
# print(id(extractor_url2)) # View memory adress

# print(f"URL size is: {len(extractor_url)}")
# print(extractor_url)
# print(extractor_url == extractor_url2)

# value_quantity = extractor_url.get_value_parameter("quantidade")
# print(value_quantity)