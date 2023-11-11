#url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = " "

# Cleaning URL
url.strip() # Also removes tab
#url = url.replace(" ", "")


# URL validation
if url == "":
	raise ValueError("URL is empty")

interrogation_index = url.find("?")

# Base
url_base = url[:interrogation_index]
print(url_base)

# Parameters
url_parameters = url[interrogation_index+1:]
print(url_parameters)

# Parameters Search
parameter_search = "quantidade"
index_parameter = url_parameters.find(parameter_search) # Searchs for where "moedaDestino" starts and return the index value
index_value = index_parameter + len(parameter_search)+1 # Gets the parameter's value index
e_commerce_index = url_parameters.find("&", index_value) # Checks if there is "&" *after the index value*
if e_commerce_index == -1:
	value = url_parameters[index_value:]
else: 
	value = url_parameters[index_value:e_commerce_index] # Value = "moedaOrigem=real&moedaDestino=dolar&quantidade=100"[12:18]
print(value)
