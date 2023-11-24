from ..code.bytebank import Employee


class TestClass:
    def test_when_birth_recieves_13_03_2000_must_return_23(self):
        input1 = "13/03/2000"  # Given-Contexto
        output1 = 23

        test_employee = Employee('Teste', input1, 1111)
        result = test_employee.age()  # When-ação

        assert result == output1  # Then-desfecho

    def test_when_surname_recieves_Lucas_Carvalho_must_return_Carvalho(self):
        input1 = "Lucas Carvalho"
        output1 = "Carvalho"

        test_employee = Employee(input1, "11/11/2000", 1111)
        result = test_employee.surname()

        assert result == output1

    def test_when_decrease_salary_recieves_100000_must_return_90000(self):
        input_salary = 100000
        input_name = "Paulo Bragança"
        output1 = 90000

        test_employee = Employee(input_name, "11/11/2000", input_salary)
        test_employee.decrease_salary()
        result = test_employee.salary

        assert result == output1
