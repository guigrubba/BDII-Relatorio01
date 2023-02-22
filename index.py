class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f'O professor {self.nome} está ministrando uma aula sobre {assunto}'

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        return f'O aluno {self.nome} está presente'

class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        aluno_anterior = ''
        for aluno in self.alunos:
            alunos_presentes = aluno_anterior + f'O aluno {aluno.nome} está presente \n'
            aluno_anterior = f'O aluno {aluno.nome} está presente \n'

professor1 = Professor("Edson")
print(professor1.ministrar_aula("Matemática"))

aluno1 = Aluno("Guilherme")
aluno2 = Aluno("Renata")
print("passei")
print(aluno1.presenca())

aula1 = Aula(professor1, "Matemática")
print(aula1.professor.nome)
aula1.adicionar_aluno(aluno1)
aula1.adicionar_aluno(aluno2)
print(aula1.alunos[0].nome)