from code.bytebank import Employee

# lucas = Employee("Lucas Carvalho", "13/03/2000", 1000)
# print(lucas)
# print(lucas.age())

def test_age():
	employee_test = Employee("Teste", "13/03/2000", 1111)
	print(f"Teste = {employee_test.age()}")

test_age()