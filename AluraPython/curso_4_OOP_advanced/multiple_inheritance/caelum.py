from worker import Worker

class Caelum(Worker):
    def show_tasks(self):
        print('Fez muita coisa, Caelumer')

    def search_monthly_courses(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')