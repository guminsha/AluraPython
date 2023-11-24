from datetime import datetime, timedelta
from date_brazil import DateBrasil
from locale import setlocale
import locale

setlocale(locale.LC_TIME, "pt-br")

login = DateBrasil()
# print(login.registration_time)
# print(login.month_registration())
print(login)

print(login.register_age())





