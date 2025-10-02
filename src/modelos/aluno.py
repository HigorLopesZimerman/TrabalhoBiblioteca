class Aluno:
    def __init__(self, codigo: int, nome: str, cod_cidade: int, cod_curso: int):
        self.codigo = codigo
        self.nome = nome
        self.cod_cidade = cod_cidade
        self.cod_curso = cod_curso

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "cod_cidade": self.cod_cidade,
            "cod_curso": self.cod_curso
        }

    @staticmethod
    def from_dict(data: dict):
        return Aluno(
            codigo=data["codigo"],
            nome=data["nome"],
            cod_cidade=data["cod_cidade"],
            cod_curso=data["cod_curso"]
        )

    def __str__(self):
        return f"Aluno {self.codigo} - {self.nome} (Cidade: {self.cod_cidade}, Curso: {self.cod_curso})"
