from datetime import datetime, timedelta
import time


class DateBrasil:
	def __init__(self) -> None:
		self.registration_time = datetime.now()

	def month_registration(self):
		return self.registration_time.month
	
	def formating_date(self):
		formated_date = self.registration_time.strftime("%H:%M:%S %d/%m/%y %A")
		return formated_date
	
	def register_age(self):
		time.sleep(3)
		register_age = datetime.now() - self.registration_time
		return register_age

	def __str__(self) -> str:
		return self.formating_date()