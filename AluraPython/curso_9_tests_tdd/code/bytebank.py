from datetime import date

class Employee:
	def __init__(self, name, birth, salary) -> None:
		self._name = name
		self._birth = birth
		self._salary = salary

	@property
	def name(self):
		return self._name
	
	@property
	def salary(self):
		return self._salary
	
	def age(self):
		birth_date_broken = self._birth.split("/")
		year_birth = birth_date_broken[-1]
		current_year = date.today().year

		return current_year - int(year_birth)

	def surname(self):
		full_name = self.name.strip()
		broken_name = full_name.split(" ")

		return broken_name[-1]

	def _is_partner(self):
		surnames = ["Bragança", "Windsor", "Bourbon", "Yamato", "Al Saud", "Khan", "Tudor", "Ptolomeu"]
		return self.salary >= 100000 and (self.surname() in surnames)

	def decrease_salary(self):
		if self._is_partner():
			decrease = self.salary * 0.1
			self._salary = self.salary - decrease

	def salary_bonus(self):
		value = self._salary * 0.1
		if value > 1000:
			value = 0
		
		return value

	def __str__(self) -> str:
		return f"Employee: {self.name}, Birth: {self._birth}, {self.salary}"