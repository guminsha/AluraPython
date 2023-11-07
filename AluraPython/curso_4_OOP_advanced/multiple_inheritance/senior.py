from alura import Alura
from caelum import Caelum
from hipster import Hipster

class Senior(Alura, Caelum, Hipster):
	def __init__(self, name) -> None:
		self.nome = name

# MIXIN