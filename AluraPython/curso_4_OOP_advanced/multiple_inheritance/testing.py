from junior import Junior
from mid_entry import MidEntry
from senior import Senior

jose = Junior()
andre = MidEntry()
paulo = Senior("Paulo")

jose.show_tasks()
andre.show_tasks() 
paulo.show_tasks()

# MRO
# Alura > Funcionario > Caelum > Funcionario

print(andre)
print(paulo)

# MIXIN

