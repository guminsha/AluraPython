from document import Document # Factory
from phone_brazil import PhoneBrasil
# from validate_docbr import CPF # pip install validate_docbr

cpf1 = Document.create_doc("12423813090")
print(cpf1)

cnpj1 = Document.create_doc("43427961000190")
print(cnpj1)

phone1 = PhoneBrasil("82912341234")
print(phone1)