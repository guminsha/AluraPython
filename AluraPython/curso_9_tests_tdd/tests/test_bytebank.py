from ..code.bytebank import Employee
import pytest
from pytest import mark

class TestClass:
    def test_when_age_receives_13_03_2000_must_return_23(self):
        input_date = "13/03/2000"  # Given-Contexto
        output = 23

        test_employee = Employee('Teste', input_date, 1111)
        result = test_employee.age()  # When-ação

        assert result == output  # Then-desfecho

    def test_when_surname_receives_Lucas_Carvalho_must_return_Carvalho(self):
        input_name = "Lucas Carvalho"
        output = "Carvalho"

        test_employee = Employee(input_name, "11/11/2000", 1111)
        result = test_employee.surname()

        assert result == output

    def test_when_decrease_salary_receives_100000_must_return_90000(self):
        input_salary = 100000
        input_name = "Paulo Bragança"
        output = 90000

        test_employee = Employee(input_name, "11/11/2000", input_salary)
        test_employee.decrease_salary()
        result = test_employee.salary

        assert result == output

    @mark.salary_bonus
    def test_when_salary_bonus_receives_1000_must_return_100(self):
        input_salary = 1000
        output = 100

        test_employee = Employee("Test", "11/11/2000", input_salary)
        result = test_employee.salary_bonus()

        assert result == output

    @mark.salary_bonus
    def test_when_salary_bonus_receives_1000000_must_return_exception(self):
        with pytest.raises(Exception):
            input_salary = 1000000

            test_employee = Employee("Test", "11/11/2000", input_salary)
            result = test_employee.salary_bonus()

            assert result