from curso import Curso
from cidade import Cidade

class Aluno:
    def __init__(self, codigo: int, nome: str, cidade: Cidade, curso: Curso):
        self.codigo = codigo
        self.nome = nome
        self.cidade = cidade
        self.curso = curso