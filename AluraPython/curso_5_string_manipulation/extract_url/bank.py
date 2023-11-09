url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)
interrogation_index = url.find("?")

url_base = url[:interrogation_index]
print(url_base)

url_parameters = url[interrogation_index+1:]
print(url_parameters)

